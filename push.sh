#!/usr/bin/env bash
REPO=$(git config remote.origin.url)
SSH_REPO=${REPO/https:\/\/github.com\//git@github.com:}

# Set up git config
git config --global user.email "monasca@lists.launchpad.net"
git config --global user.name "Monasca CI"

# Build Helm Charts
helm repo add monasca http://monasca.io/monasca-helm/

for chart in "$@"
do
 helm dependency update "$chart"
 helm package "$chart"
done

# clone repo to make changes in
git clone $REPO out
cd out
git checkout gh-pages
cd ..

# copy over packages
cp *.tgz out/.

# Update index file
cd out
helm repo index . --url http://monasca.io/monasca-helm/

# Commit changes
git add *.tgz
git add index.yaml
git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"

# Push Changes
chmod 600 deploy-key
eval "$(ssh-agent -s)"
ssh-add deploy-key
git push "$SSH_REPO" gh-pages

# Remove out directory
cd ..
rm -rf out
git checkout -- .

# check out master branch again to create pull requests
git status
