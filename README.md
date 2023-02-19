<p align="center">
  <a title="msys2.github.io" href="https://msys2.github.io"><img src="https://img.shields.io/website.svg?label=msys2.github.io&longCache=true&style=flat-square&url=http%3A%2F%2Fmsys2.github.io%2Findex.html&logo=github"></a><!--
  -->
  <a title="Join the chat on Matrix" href="https://matrix.to/#/#msys2_msys2:gitter.im"><img src="https://img.shields.io/badge/chat-on%20matrix-4db797.svg?longCache=true&style=flat-square&logo=matrix&logoColor=e8ecef"></a><!--
  -->
  <a title="GitHub Actions" href="https://github.com/msys2/msys2.github.io/actions?query=workflow%3Agithub%20pages"><img alt="github pages' workflow Status" src="https://img.shields.io/github/actions/workflow/status/msys2/msys2.github.io/main.yml?branch=source&longCache=true&style=flat-square&label=build&logo=github"></a><!--
  -->
  <a title="Follow msys2org on Twitter" href="https://twitter.com/msys2org"><img src="https://img.shields.io/twitter/follow/msys2org?color=31A4F1&logo=twitter&logoColor=white&style=flat-square"></a><!--
  -->
  <a title="Follow msys2org on Mastodon" href="https://fosstodon.org/@msys2org"><img src="https://img.shields.io/mastodon/follow/109365079526574177?color=000197&domain=https%3A%2F%2Ffosstodon.org%2F&logo=mastodon&logoColor=white&style=flat-square"></a><!--
  -->
  <a title="Join the community on Discord" href="https://discord.com/invite/jPQdRdDcT9"><img src="https://img.shields.io/discord/792780131906617355?color=5865F2&label=Discord&logo=discord&logoColor=white&style=flat-square"></a><!--
  -->
</p>

# MSYS2 Website

## Overview

This website is written in Markdown and gets built to a static website using
[mkdocs](https://www.mkdocs.org/) and a modified version of the [mkdocs-material
theme](https://squidfunk.github.io/mkdocs-material). The main branch of this
repo is the `source` branch and any new commits will auto deploy a new build to
the `main` branch using [a GitHub
action](https://github.com/peaceiris/actions-gh-pages). The `main` branch is
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
