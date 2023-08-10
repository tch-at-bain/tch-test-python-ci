# Semantinc Releases

  Detect the semantically correct next version that should be applied to your
  project.

  By default:
    *Write this new version to the project metadata locations
      specified in the configuration file
    * Create a new commit with these locations and any other assets configured
      to be included in a release
    *Tag this commit according the configured format, with a tag that uniquely
      identifies the version being released.
    * Push the new tag and commit to the remote for the repository
    * Create a release (if supported) in the remote VCS for this tag

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

- Pre-releases can be triggered using cli and `--prerelease` option: <https://python-semantic-release.readthedocs.io/en/latest/commands.html#prerelease> and specific version bump -> see below.

TODO: this doesnt work currently - config for multibranch releases required?

- Release of specific version can be triggered using `--major`, `--minor` and `--patch` types.

````bash
semantic-release -v version --minor
````

TODO: This outputs a bug (related to missing v1.1.0 tag ) but seems to be working. No tag created though.
TODO: [semantic_release.cli.commands.version] ERROR version.version: release id for tag v1.1.0 not found, and could not be created

## Cons

- Need to be disciplined with commits and their commit messages
- Could be sutiable for plato-core, less so for plato-apps

oo