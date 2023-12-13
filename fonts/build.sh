#!/bin/bash

set -e

rm -Rf ../overrides/fonts/*

# See ../web/stylesheets/fonts.css for which files are needed
mkdir -p ../overrides/fonts/chivo
cp -R node_modules/@fontsource/chivo/latin-{400,700,900}.css ../overrides/fonts/chivo
mkdir -p ../overrides/fonts/chivo/files
cp -R node_modules/@fontsource/chivo/files/chivo-latin-{400-normal,700-normal,900-normal}.woff2 ../overrides/fonts/chivo/files

mkdir -p ../overrides/fonts/roboto
cp -R node_modules/@fontsource/roboto/latin-{300,400,400-italic,700}.css ../overrides/fonts/roboto
mkdir -p ../overrides/fonts/roboto/files
cp -R node_modules/@fontsource/roboto/files/roboto-latin-{300-normal,400-normal,400-italic,700-normal}.woff2 ../overrides/fonts/roboto/files

mkdir -p ../overrides/fonts/roboto-mono
cp -R node_modules/@fontsource/roboto-mono/latin-400.css ../overrides/fonts/roboto-mono
mkdir -p ../overrides/fonts/roboto-mono/files
cp -R node_modules/@fontsource/roboto-mono/files/roboto-mono-latin-400-normal.woff2 ../overrides/fonts/roboto-mono/files
