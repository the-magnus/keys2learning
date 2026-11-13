# Changelog

Notable changes to keys2learning. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and a version is two numbers, such as 0.8: the second goes up by one with each release, as far as it needs to. Releases up to 0.7.0 were written with a third number, which was always zero. Before 1.0, any release may change files and formats.

## [0.8] - 2026-11-13

### Fixed

1. **Setting up a Claude Project needs one pasted sentence after all.** Versions 0.6 and 0.7 said to add the file and say hello. In a Project that does not load its files until they are asked for, the tutor then answered as an ordinary assistant. The README and the built file now give one sentence to paste into the Project's instructions. Tried once in a new Project: with the sentence in place, the tutor read the file and welcomed the learner in its first reply.

## [0.7.0] - 2026-11-13

### Added

1. **A thread for every module:** a new part, after the Idea, that says how the module's thinkers answer its question together. A learner had found the thinkers of module 1 loosely connected.
2. **Four stories from the thinkers themselves,** each checked on a source's own page or marked as from summaries: Snowden's children's party and Sarasvathy's kitchen in module 1, Rumelt's moon landing in module 2, and Minard's map in module 6.

### Changed

1. **No point is marked unconfirmed any more.** Rother's target condition now follows his *Improvement Kata Handbook*. Dettmer's eight Categories of Legitimate Reservation are listed from chapter 1 of his book. That a problem can sit in many domains follows the Cynefin wiki.
2. Module 1: "one manages the constraints, not the outcome" had no source, and the Cynefin wiki keeps "manage the constraints" for the Theory of Constraints. It now reads: constraints bias the system; they don't fix what it does.
3. **Module 5's third concept is rebuilt around the idea, not one guide.** "What must hold is built around the model" now rests first on Birgitta Böckeler's guides and sensors, computational or inferential, with Alexey Krivitsky's ladder and Anthropic's advice for how far to go, and says that practitioners agreeing is not evidence.

### Known gaps

1. Stories looked for and not confirmed, so left out: Snowden's engine and rainforest, the crux as a climbing term, and Kahneman and Klein's examples.
2. Modules 6 and 7 still rest on theory alone; studies that test Tufte, and critiques of effectuation, are not yet in the textbook.
3. OpenAI's account of harness engineering could not be read, and is not cited.

## [0.6.0] - 2026-11-13

### Changed

1. **`programs/tutoring.md` is rewritten, purpose first.** It says what the tutor is for, what the learner can choose, the three things that do not bend, and how the workbook and progress are kept. The step lists for a session and a first session, the three scripted styles and the timings are gone: they told the tutor what to do without saying why, and it followed the form past its purpose.
2. **A first session opens with a welcome,** not with questions. What the learner wants to be able to do, and where they stand, are asked when a lesson first reaches for their own work.
3. **The learner chooses how to learn:** reading or listening as from a textbook, the same with a few questions, a full session on Bowman's 4Cs, or help applying a module to their work. These replace the interactive, podcast and trialogue styles.
4. **A program is two files,** `about.md` and `textbook.md`. What a tutor needs away from the desk is a section of `tutoring.md`, and the release file opens with four sentences to the model, written by `development/bundle.py`, so nothing is pasted into the Project's instructions. The release file is now `dist/<program>.md`, for voice or text.
5. **The tutor saves the workbook itself where it can,** in a Claude Project too; where it can't, it tells the learner what to copy in.
6. `programs/` no longer points into `development/`, so a program can be read on its own.
7. `about.md` says what the program takes: what you need, and roughly how many sittings.

### Removed

1. `voice_tutor.md`, the instruction written per program.
2. The subtitle *Don't panic: a hitchhiker's guide*, and the tutor's leave to be playful. A style for a program is to be tried for its effect before it goes in.

## [0.5.0] - 2026-11-12

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
