<p align="center">
  <a title="msys2.github.io" href="https://msys2.github.io"><img src="https://img.shields.io/website.svg?label=msys2.github.io&longCache=true&style=flat-square&url=http%3A%2F%2Fmsys2.github.io%2Findex.html&logo=github"></a><!--
  -->
  <a title="Join the chat at https://gitter.im/msys2/msys2" href="https://gitter.im/msys2/msys2"><img src="https://img.shields.io/badge/chat-on%20gitter-4db797.svg?longCache=true&style=flat-square&logo=gitter&logoColor=e8ecef"></a><!--
  -->
  <a title="GitHub Actions" href="https://github.com/msys2/msys2.github.io/actions?query=workflow%3Agithub%20pages"><img alt="github pages' workflow Status" src="https://img.shields.io/github/workflow/status/msys2/msys2.github.io/github%20pages?longCache=true&style=flat-square&label=build&logo=github"></a><!--
  -->
</p>

# MSYS2 Website

## Overview

This website is written in Markdown and gets built to a static website using
[mkdocs](https://www.mkdocs.org/) and a modified version of the [mkdocs-material
theme](https://squidfunk.github.io/mkdocs-material). The main branch of this
repo is the `source` branch and any new commits will auto deploy a new build to
the `master` branch using [a GitHub
action](https://github.com/peaceiris/actions-gh-pages). The `master` branch is
connected to [GitHub pages](https://pages.github.com) and is reachable under
https://msys2.github.io and https://www.msys2.org. Changes to the `source`
branch usually take a minute or two until they are live.


## Development

For small changes:

* Just use the online editor on GitHub and use the Markdown preview to inspect your changes
* Open a PR with your changes in case you don't have commit rights
* **Note:** The Markdown dialect and extensions understood by mkdocs and GitHub is
  slightly different, so double check that the deployed website matches what you
  expected
* **Note:** Every page on the website has a small "edit" icon in the top right corner which leads you straight to the online editor for that page

For larger changes:

* `poetry install`
* `poetry run mkdocs serve`
* Access http://127.0.0.1:8000 - any changes to the sources should be
  immediately visible in your browser
* Open a PR with your changes or just push them if you have commit rights
