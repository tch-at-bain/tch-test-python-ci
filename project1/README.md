# Semantinc Releases

docs: <https://python-semantic-release.readthedocs.io/en/latest/index.html>

## Key Feature

- Automated versioning, customisable - tested
- releases (artefacts) - tested (no pypi tested yet)
- Integrated with poetry - tested
- Maintains version numbers in code and pyproject.toml (TODO: fix in-code version maintenance)
- Generates changelog - tested
- Changelog templates - not tested
- Monorepo support - tested (single repo though, how to reduce gha definnitions)
- support for multi-branch workflows (not-tested)

## Automated Releases

Relies on structure and content of commit message to decide on version bump

1. Structure your commit messages following guidelines here: <https://python-semantic-release.readthedocs.io/en/latest/commit-parsing.html#semantic-release-commit-parser-angularcommitparser>

1.1 Major number changes follow more specific structure

````text
feat(scope): added options

fixes feature by

BREAKING CHANGE: breaking change summary

breaking change description and migration instructions


Fixes #issue number
````

Notice two blanks lines after breaking change description - it wont work if the format is not followed to the blank line

## On demand releases

Pre-releases can be triggered using cli and `--prerelease` option: <https://python-semantic-release.readthedocs.io/en/latest/commands.html#prerelease>

Release of specific version can be triggered using `--major`, `--minor` and `--patch` types.

## Cons

- Need to be disciplined with commits and their commit messages
- Could be sutiable for plato-core, less so for plato-apps
