# Changelog

Notable changes to keys2learning. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Before 1.0, any release may change files and formats.

## [Unreleased]

### Added

1. **An assisted start.** A learner without a workbook is started off by the tutor without asking for it: at the desk after a hello, and by voice in a Claude Project that holds no workbook yet. `programs/tutoring.md` has a "First session" section, and the README's "How to use it" is three steps for each way in.
2. **Progress.** The tutor says where the learner stands at the start and the end of every session: modules built, the module in hand and its state, and Must cover points landed. Each module's section in the workbook starts with its state.
3. **An easier installation.** At the desk, one sentence to Claude Code clones the repository and starts the tutor. For voice, each release carries one voice file per program, built by `development/bundle.py`, in place of three files and a pasted text.
4. **Feedback to the program.** At the end of a first session, and when a module is built, the tutor offers to help write a short note in the three parts of the feedback form, with nothing private in it. The learner sends it themselves.

## [0.4.0] - 2026-11-12

### Changed

1. Module 4, "Agents as team members", is split in two, since it held two subjects and its Build asked for two pieces. Module 4 keeps working with an agent as a team member: joint activity, the ten challenges, when a quick judgement can be trusted, and the coupled system. The new module 5, "Building around the model", takes context as a scarce resource, tests as the agent's feedback, engineering the system around the model, and rules as constraints. No concept, source or Must cover point was added or removed; the new module's Idea, Reason and Brings are new text.
2. The program has seven modules. "Seeing it at a glance" is now module 6 and "Staying well in it" module 7; earlier entries in this file use the old numbers. A workbook that names modules 5 or 6 by number means the old ones.

### Added

1. The textbook's overview says how many listening sittings each module takes, estimated from its number of concepts.

## [0.3.0] - 2026-11-12

### Changed

1. The program "Building with agents and science" has a subtitle: *Don't panic: a hitchhiker's guide*, to add humour. `about.md` says what "don't panic" means for the program, and the voice tutor may be lightly playful while the evidence stays sober.

## [0.2.0] - 2026-11-12

### Changed

1. Modules 3 and 6: eleven concepts that were one line each now say what the concept is, name the thinker's own case where a checked one exists, and say what it means in a system of a person and agents, marked *(the tutor's link)*.
2. Module 6: "The constraint may be a person" is now "The constraint may be skilled labour", the wording its source supports. Two Must cover points are reworded to what the sources say: the loss accepted is decided at each step, and subordinating means everything else is aligned to the constraint.
3. Modules 3 and 6 list the pages their concepts were checked against.

### Fixed

1. Module 1: "one manages the constraints, not the outcome" had no source and no mark. It is now marked *(unconfirmed)*.
2. Module 3: the Categories of Legitimate Reservation no longer imply a fixed count. Summaries list from seven to ten, and Dettmer's own list is marked *(unconfirmed)*.

### Known gaps

1. Dettmer's book, Goldratt's own text, Sarasvathy's 2001 paper and Klein's full article were not reached; the check rests on institute pages and summaries.

## [0.1.0] - 2026-11-12

First public version.

### Added

1. The program "Building with agents and science": six modules, each with its concepts, sources marked by kind of evidence, a question to reason through, a build, and the points the tutor must cover.
2. `programs/tutoring.md`: how each session runs, in three styles (interactive, podcast, trialogue).
3. `development/making.md`: a guide to making a program. `development/notes.md`: how the program came to be. `development/index.html`: two diagrams of the structure.
4. `CLAUDE.md`: rules for an agent that tutors or helps make a program.
5. README with what the project claims and does not claim, the CC BY 4.0 licence, a contributing guide, a code of conduct, a security and privacy note, and issue and pull request templates.

### Known gaps

1. No intake for a new learner.
2. The voice tutor's progress summary is copied into the workbook by hand.
3. Some concepts are stated briefly, because the earlier programs that taught them at length are not published.

[0.3.0]: https://github.com/the-magnus/keys2learning/releases/tag/v0.3.0
[0.2.0]: https://github.com/the-magnus/keys2learning/releases/tag/v0.2.0
[0.1.0]: https://github.com/the-magnus/keys2learning/releases/tag/v0.1.0
