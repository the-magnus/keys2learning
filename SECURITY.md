# Security and privacy

This repository holds text and one static HTML page (`development/index.html`, which loads the Mermaid library from a public CDN). There is no software to install and no service to attack.

## What to report

1. **Private information** that should not be in the repository or its history: a learner's name, a workbook, a personal detail.
2. **A harmful link** among the sources.
3. **Instructions that could make an agent act against the learner,** in `CLAUDE.md`, `programs/tutoring.md` or a `voice_tutor.md`.

## How to report

Do not repeat the private information in a public issue. Use GitHub's private report form: the repository's **Security** tab, then **Report a vulnerability** (https://github.com/the-magnus/keys2learning/security/advisories/new). Only the maintainer can read what you send there. If the form is not available, open an issue that says only that you have a private report, and the maintainer will arrange a private channel. Reports under the [code of conduct](CODE_OF_CONDUCT.md) go through the same form.

## Your own data

Your workbook lives in a `local/` folder that git ignores. That keeps it out of git only. What you send to an AI provider is handled under that provider's terms, and backing the workbook up is your responsibility.
