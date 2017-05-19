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

# Set up key to push
ENCRYPTED_KEY_VAR="encrypted_${ENCRYPTION_LABEL}_key"
ENCRYPTED_IV_VAR="encrypted_${ENCRYPTION_LABEL}_iv"
ENCRYPTED_KEY=${!ENCRYPTED_KEY_VAR}
ENCRYPTED_IV=${!ENCRYPTED_IV_VAR}
openssl aes-256-cbc -K $ENCRYPTED_KEY -iv $ENCRYPTED_IV -in ../deploy_key.enc -out ../deploy_key -d
chmod 600 ../deploy-key
eval "$(ssh-agent -s)"
ssh-add ../deploy-key

# Push Changes
git push "$SSH_REPO" gh-pages

# Remove out directory
cd ..
rm -rf out
git checkout -- .

# check out master branch again to create pull requests
git status
