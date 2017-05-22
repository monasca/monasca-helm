#!/usr/bin/env python

# (C) Copyright 2017 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

from __future__ import print_function

import os
import signal
import subprocess
import sys

import yaml


class SubprocessException(Exception):
    pass

class FileReadException(Exception):
    pass

def get_changed_files():
    commit_range = os.environ.get('TRAVIS_COMMIT_RANGE', None)
    if not commit_range:
        return []

    p = subprocess.Popen([
        'git', 'diff', '--name-only', commit_range
    ], stdout=subprocess.PIPE)

    stdout, _ = p.communicate()
    if p.returncode != 0:
        raise SubprocessException('git returned non-zero exit code')

    return [line.strip() for line in stdout.splitlines()]


def get_dirty_modules(dirty_files):
    dirty = set()
    for f in dirty_files:
        if os.path.sep in f:
            mod, _ = f.split(os.path.sep, 1)

            if not os.path.exists(os.path.join(mod, 'Chart.yaml')):
                continue

            dirty.add(mod)

    return list(dirty)


def get_dirty_for_module(files, module=None):
    ret = []
    for f in files:
        if os.path.sep in f:
            mod, rel_path = f.split(os.path.sep, 1)
            if mod == module:
                ret.append(rel_path)
        else:
            # top-level file, no module
            if module is None:
                ret.append(f)

    return ret


def run_verify(modules):
    build_args = ['./helm', 'lint'] + modules

    print('verify command:', build_args)

    p = subprocess.Popen(build_args, stdin=subprocess.PIPE)

    def kill(signal, frame):
        p.kill()
        print()
        print('killed!')
        sys.exit(1)

    signal.signal(signal.SIGINT, kill)
    if p.wait() != 0:
        print('lint failed, exiting!')
        sys.exit(p.returncode)


def run_push(modules):
    if os.environ.get('TRAVIS_SECURE_ENV_VARS', None) != "true":
        print('No push permissions in this context, skipping!')
        print('Not pushing: %r' % modules)
        return

    push_args = ['./push.sh'] + modules
    print('push command:', push_args)

    p = subprocess.Popen(push_args, stdin=subprocess.PIPE)

    def kill(signal, frame):
        p.kill()
        print()
        print('killed!')
        sys.exit(1)

    signal.signal(signal.SIGINT, kill)
    if p.wait() != 0:
        print('push failed, exiting!')
        sys.exit(p.returncode)


def handle_pull_request(files, modules):
    if modules:
        run_verify(modules)
    else:
        print('No modules to verify.')


def check_version_change(module):
    chart_path = module + "/Chart.yaml"
    commit_range = os.environ.get('TRAVIS_COMMIT_RANGE', None)

    p = subprocess.Popen([
        'git', 'diff', '-G', 'version', commit_range, chart_path
    ], stdout=subprocess.PIPE)

    stdout, _ = p.communicate()
    if p.returncode != 0:
        raise SubprocessException('git returned non-zero exit code')

    if len(stdout) == 0:
        return None

    try:
        with open(chart_path) as chart:
            chart_dict = yaml.load(chart_path)
    except:
        raise FileReadException('Error reading chart yaml for changed chart')

    return chart_dict['version']


def build_requirements_dictionary(updated_modules):
    return_requirements = {}
    for module in next(os.walk('.'))[1]:
        if not os.path.exists(os.path.join(module, 'requirements.yaml')):
            continue
        try:
            with open(module + "/requirements.yaml") as requirements:
                requirement_dict = yaml.load(requirements)
        except:
            raise Exception('Error reading requirements yaml for changed chart')
        if not requirement_dict or "dependencies" not in requirement_dict:
            continue
        for dependency in requirement_dict['dependencies']:
            dependency_name = dependency['name']
            if dependency_name in updated_modules:
                dependency['version'] = updated_modules[dependency_name]
                if module not in return_requirements:
                    return_requirements[module] = requirement_dict
    return return_requirements


def handle_push(files, modules):
    if modules:
        run_verify(modules)
    else:
        print('No modules to verify.')
        return

    modules_updated = {}
    for module in modules:
        dirty = get_dirty_for_module(files, module)

        if 'Chart.yaml' in dirty:
            version = check_version_change(module)
            if version != None:
                modules_updated[module] = version

    if modules_updated:
        run_push(modules_updated.keys())
        pr_dictionary = build_requirements_dictionary(modules_updated)
        print('Module requirements to update')
        print(pr_dictionary)
    else:
        print('No modules to push.')

def handle_other(files, modules, tags):
    print('Unsupported event type "%s", nothing to do.' % (
        os.environ.get('TRAVS_EVENT_TYPE')))


def main():
    print('Environment details:')
    print('TRAVIS_COMMIT=', os.environ.get('TRAVIS_COMMIT'))
    print('TRAVIS_COMMIT_RANGE=', os.environ.get('TRAVIS_COMMIT_RANGE'))
    print('TRAVIS_PULL_REQUEST=', os.environ.get('TRAVIS_PULL_REQUEST'))
    print('TRAVIS_PULL_REQUEST_SHA=',
          os.environ.get('TRAVIS_PULL_REQUEST_SHA'))
    print('TRAVIS_PULL_REQUEST_SLUG=',
          os.environ.get('TRAVIS_PULL_REQUEST_SLUG'))
    print('TRAVIS_SECURE_ENV_VARS=', os.environ.get('TRAVIS_SECURE_ENV_VARS'))
    print('TRAVIS_EVENT_TYPE=', os.environ.get('TRAVIS_EVENT_TYPE'))
    print('TRAVIS_BRANCH=', os.environ.get('TRAVIS_BRANCH'))
    print('TRAVIS_PULL_REQUEST_BRANCH=',
          os.environ.get('TRAVIS_PULL_REQUEST_BRANCH'))
    print('TRAVIS_TAG=', os.environ.get('TRAVIS_TAG'))
    print('TRAVIS_COMMIT_MESSAGE=', os.environ.get('TRAVIS_COMMIT_MESSAGE'))

    if os.environ.get('TRAVIS_BRANCH', None) != 'master':
        print('Not master branch, skipping tests.')
        return

    files = get_changed_files()
    modules = get_dirty_modules(files)

    func = {
        'pull_request': handle_pull_request,
        'push': handle_push
    }.get(os.environ.get('TRAVIS_EVENT_TYPE', None), handle_other)

    func(files, modules)


if __name__ == '__main__':
    main()
