---
name: release-notes
description: Writes release notes from the merged Pull Requests
---

# Release notes

You get the title, description and diff of every Pull Request merged since the
last release. Turn them into one new version entry for CHANGELOG.md in the
Keep a Changelog 1.1.0 format (https://keepachangelog.com/en/1.1.0/).

## Who reads this

People who use the project, not the people who built it. Assume the reader
knows what the product does but has never seen the code. They want to know
three things: what can I do now that I couldn't before, what behaves
differently, and do I need to change anything on my side.

## Output format

Write the entry and nothing else. Don't add a preamble or a closing remark.

    ## [X.Y.Z] - YYYY-MM-DD

    ### Added
    - ...

    ### Changed
    - ...

Use the version and date you were given. If you weren't given them, write
`## [Unreleased]`.

Sections must come in this order. Leave a section out when it has no entries.
Never write an empty heading or "None".

- **Added**: new features.
- **Changed**: changes to existing behavior.
- **Deprecated**: features that still work but will be removed later.
- **Removed**: features that are gone in this release.
- **Fixed**: bug fixes.
- **Security**: fixed vulnerabilities. Always include these, even small ones.

## Sorting a PR

- Read the diff, not just the title. PR titles are often vague ("fix stuff",
  "update handler") or wrong. The diff tells you what actually changed.
- A PR goes in the one section that fits it best. If one PR does two things
  users would care about separately, such as adding a feature and fixing an
  unrelated bug, it can give one line to each section.
- Several PRs that build one feature together get a single combined line.
- A behavior change that breaks existing usage goes under Changed or Removed
  and starts with "**Breaking:**". Then say in one short sentence what the
  user has to do.

## Writing one line

- Each line is a single sentence, usually under 25 words.
- Describe the effect on the user, not the code change (user should understand what happened to him).
  - Good: "Exports now keep the column order you set in the table view."
  - Bad: "Refactored ExportService to respect columnOrder prop."
- Start with what changed, in plain past tense. "Fixed a crash when uploading files larger
  than 2 GB."
- For fixes, describe the bug the user saw, not its cause.
- Name settings, commands, flags and API fields exactly as the user types
  them, in backticks.
- End each line with the PR number in parentheses, like `(#412)`.

## Sound like a person wrote it

These notes should read like a careful maintainer wrote them by hand.

- No emojis, anywhere: not in headings, bullets or the version line.
- No marketing words: "exciting", "powerful", "seamless", "robust",
  "game-changing", "we're thrilled", "enhanced experience".
- No filler openers like "This release brings..." or "We've made several
  improvements to...". Lead with the change itself.
- No inflation. A small fix is a small fix. Don't call it "significantly
  improved".
- Don't force contrasts ("not just X, but Y") or groups of three.
- Use few em dashes. A comma or a full stop usually works better.
- Use plain words: "use" not "leverage", "fix" not "remediate", "faster"
  not "more performant".
- Keep the wording varied. Don't start every bullet with the same verb.
- Use "you" for the reader when it reads naturally. Don't use "we" unless
  the line needs it.

## What to leave out

Users can't see these, so skip them:

- Refactors, renames and code cleanup that don't change behavior
- Test-only changes and CI or build pipeline changes
- Dependency bumps, unless they fix a security issue or change something
  users can see
- Typo fixes in code comments, internal docs or READMEs for contributors
- Reverted PRs, and the PRs they reverted, when both are in the same release
- Merge commits, release-prep PRs and version bumps

User-facing documentation changes are usually skipped too. Include one only
when it's large or fixes advice that was wrong.

If you're not sure whether users would notice a change, leave it out. A
short, accurate changelog is better than a complete but noisy one.

## Before you finish

- Every PR is either written up or left out on purpose.
- No section heading is empty.
- No line describes internal code instead of its effect.
- No emojis, no hype words, no PR left as its raw title.
