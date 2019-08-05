#!/bin/bash

if [ -z $1 ]
then
	echo "Please provide a tag argument."
    exit 1;
fi
if [[ $(git status -s) ]]
then
    echo "The working directory is dirty. Please commit any pending changes."
    exit 1;
fi

set -e

echo "Deleting old publication"
rm -rf _build

echo "Building docs"
sphinx-apidoc -o reference/api/ ../tac/
make html
cd ..

echo "Create a local gh-pages branch containing the splitted output folder"
git subtree split --prefix docs/_build -b gh-pages

echo "Pushing to gh-pages branch"
git add --all && git commit -m "Publishing to gh-pages with tag $1"
git tag $1
git pull origin gh-pages
git push origin gh-pages:gh-pages


echo "Delete local gh-pages"
git branch -D gh-pages