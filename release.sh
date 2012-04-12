#!/bin/bash

RELEASE_NUM=`grep VERSION csvfilter/__init__.py | cut -d\' -f2`

git tag | grep $RELEASE_NUM > /dev/null && \
	echo "New version number required ($RELEASE_NUM already used)" && exit 1
echo "Releasing version $RELEASE_NUM"

# Push to PyPi
./setup.py sdist upload

# Tag in Git
git tag $RELEASE_NUM -m "Tagging release $RELEASE_NUM"
git push origin master
git push --tags