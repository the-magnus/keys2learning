# keys2learning

Learning programs taught by an AI tutor. A program gathers the thinkers whose research answers a question you have. The tutor then teaches them on your own work, not on textbook cases. Curated by Keys2Collaboration (K2C).

**Version 0.1.** This is an early start: one program, made for one learner. Read [What to expect, and what not](#what-to-expect-and-what-not) before you rely on any of it.

## What is here

1. **One program:** [Building with agents and science](programs/building-with-agents-and-science/about.md). Six modules for someone who builds a system in which they and AI agents work toward targets. Each module ends in a piece of your own system.
2. **How a session runs:** [`programs/tutoring.md`](programs/tutoring.md). The tutor follows it in every session. It has three styles: interactive, podcast and trialogue.
3. **How a program is made:** [`development/making.md`](development/making.md), a guide. [`development/notes.md`](development/notes.md) records how the program came to be and who decided what. [`development/index.html`](development/index.html) has two diagrams of the structure.
4. **Rules for the agent:** [`CLAUDE.md`](CLAUDE.md). A coding agent that opens this folder reads them and acts as the tutor.

A program is four files:

| File | What it holds |
|---|---|
| `about.md` | What the program is, why, and its thinkers |
| `textbook.md` | The lessons or modules, with sources |
| `voice_tutor.md` | Instructions for a tutor you talk with |
| `local/workbook.md` | Your starting point and progress. Private, and never in git |

## How to use it

You need your own access to an AI model. The program was made and tried with Anthropic's Claude: Claude Code at the desk and a Claude Project for voice. Both may cost money.

1. Clone the repository.
2. Read the program's [`about.md`](programs/building-with-agents-and-science/about.md) to see if its question is yours.
3. **At the desk:** open the folder in Claude Code and ask the tutor to start your workbook for the program. It reads where you stand, names with you what you want to be able to do, and writes `local/workbook.md` (steps 1, 2 and 6 of `development/making.md`). After that, ask for a session.
4. **By voice:** create a Claude Project. Add `about.md`, `textbook.md`, your `workbook.md` and `tutoring.md`, and paste the text from `voice_tutor.md` as its instructions. At the end of a session the tutor says a progress summary. Copy it into your workbook yourself: the Project can't write files.

Each module has three parts: listen (by voice), build (at the desk, with an agent) and conclude. You pick and pace.

## What to expect, and what not

### What it claims

1. **Sources are named.** Each concept names its thinker, and each module lists where to read them.
2. **Each source is marked with its kind of evidence:** review, trial, study, benchmark, theory, practice or summary. A claim can then be weighed by what stands behind it.
3. **What was not confirmed is marked.** A point marked *(unconfirmed)* was not found in a source when it was checked. A point marked *(the tutor's link)* joins two sources in a way neither of them does.
4. **The tutoring follows published methods:** Bowman's 4Cs, retrieval practice and deliberate practice. `programs/tutoring.md` names them.
5. **Your workbook stays out of git.** Every `local/` folder is git-ignored.

### What it does not claim

1. **It is not shown to work.** The program was made in November 2026 for one learner, its curator. No one has completed it. Nobody has measured what a learner learns from it.
2. **It is not checked against the original works.** An AI model (Claude) wrote the text at the curator's request and under his direction. The sources were checked by web search, mostly against secondary summaries, on the dates the textbook gives. Some figures were checked against the papers themselves. Expect errors. Read the source before you rely on a claim.
3. **It does not speak for the thinkers.** The summaries are short and are an interpretation. None of the people named has reviewed or endorsed this. In the trialogue style the tutor voices the thinkers; that is the tutor's interpretation, not their words. The summaries do not replace their books and papers.
4. **It is not affiliated with Anthropic,** nor endorsed by it. It has been tried only with Claude. Other models and agents may work; nobody has tried.
5. **The tutor can be wrong.** An AI tutor can state things with confidence that are false, and can go beyond the textbook. Treat what it says as a claim to test.
6. **It is not professional advice.** Not business, legal, financial, medical or psychological advice. Module 6, "Staying well in it", is about how a builder works. It is not health advice.
7. **It does not keep your data private from your AI provider.** What you tell the tutor, and what you put in a Claude Project, goes to the provider under its terms. The git-ignore rule only keeps your workbook out of git. Backing your workbook up is your responsibility.
8. **It is not complete or stable.** Before version 1.0, files and formats can change without notice.

### Known gaps

1. **No intake for a new learner.** `making.md` says to read where the learner stands, but not yet how a new learner joins an existing program. The route under "How to use it" has not been tried by a second learner.
2. **The voice tutor's summary is copied by hand** into the workbook.
3. **Some concepts are stated briefly.** Two earlier programs taught them at more length and are not published. This shows most in modules 3 and 6.
4. **Each program writes its own voice tutor.** There is no shared template yet.

## Contributing

Issues and pull requests are welcome. The most useful ones correct a source or report what happened when you tried a session. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md). Never put a workbook, or anyone's private case, in an issue or a pull request.

## Licence and credit

© 2026 Magnus Vestin, Keys2Collaboration. The text of this repository is licensed under [Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0). You may use it, change it and share it, also commercially, if you give credit. For example:

> keys2learning by Magnus Vestin, Keys2Collaboration, CC BY 4.0. https://github.com/the-magnus/keys2learning

The licence comes with no warranty. It covers this repository's own text. The books, papers and reports it cites belong to their authors and publishers, and the product names it mentions belong to their owners.

## Thanks

1. Sharon Bowman, for the 4Cs in *Training from the Back of the Room!*
2. The thinkers the program rests on. They are named in its [`about.md`](programs/building-with-agents-and-science/about.md).
