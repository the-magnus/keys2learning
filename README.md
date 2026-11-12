# keys2learning

Learning programs taught by an AI tutor. A program gathers the thinkers whose research answers a question you have. The tutor then teaches them on your own work, not on textbook cases. Curated by Keys2Collaboration (K2C).

**Version 0.5:** one program so far, and young. [What to expect](#what-to-expect-and-what-not) says what it does well and where it is still thin.

## What is here

1. **One program:** [Building with agents and science: Don't panic, a hitchhiker's guide](programs/building-with-agents-and-science/about.md). Seven modules for someone who builds a system in which they and AI agents work toward targets. Each module ends in a piece of your own system.
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

You need your own access to an AI model. The program was made and tried with Anthropic's Claude: Claude Code at the desk and a Claude Project for voice. Both may cost money. Read the program's [`about.md`](programs/building-with-agents-and-science/about.md) first, to see if its question is yours.

### At the desk

1. Start Claude Code in a folder where the program may live, and tell it: "Clone https://github.com/the-magnus/keys2learning and start the tutor."
2. Or do it by hand: clone the repository, or download it as a ZIP and unpack it, and open the folder in Claude Code.
3. Say hello. The tutor sees that you have no workbook yet and starts you off: it reads where you stand, names with you what you want to be able to do, and writes `local/workbook.md`. After that, ask for a session.

### By voice

1. Download the program's voice file from the [latest release](https://github.com/the-magnus/keys2learning/releases/latest), create a Claude Project and add the file to it. If you already have a workbook from the desk, add it too.
2. Copy the part of the file headed "Instructions to paste" into the Project's instructions.
3. Start a voice conversation and say hello. Without a workbook, the tutor starts you off and says your workbook's opening at the end: save it as `workbook.md` and add it to the Project. At the end of each later session it says a progress summary. Copy it into your workbook yourself: the Project can't write files.

### As you go

1. Each module has three parts: listen (by voice), build (at the desk, with an agent) and conclude. You pick and pace.
2. The tutor tells you where you stand at the start and the end of each session: how many modules you have built, and how far you are in the one in hand.
3. When you have built a module, the tutor offers to help you write a short note to us on what worked and what didn't. You send it yourself, or not at all.

## What to expect, and what not

### What you get

1. **You learn on your own work.** The tutor reads where you stand and teaches each concept on the system you are building, not on textbook cases. Each module ends in a working piece of that system.
2. **You learn where you are.** By voice while you drive or walk, at the desk with an agent, or both. Hear a module as a podcast, talk it through, or listen to the thinkers argue it out in a trialogue.
3. **You learn from the people who did the research.** Each concept names its thinker and where to read them. The tutoring itself follows published methods: Bowman's 4Cs, retrieval practice and deliberate practice.
4. **You can see what each claim stands on.** Every source is marked as a review, trial, study, benchmark, theory, practice or summary. Points that were not found in a source are marked *(unconfirmed)*, and a link the tutor makes between two sources is marked *(the tutor's link)*. Few courses tell you this much.
5. **Your workbook stays yours.** It lives in a `local/` folder that git ignores.

### What could happen

Not promised, and so far one learner's account. An early learner tried an earlier program by voice, on free Claude:

1. It worked really well, even on the free plan.
2. At first the tutor asked too many questions for driving. Once told to just talk, it got really good.
3. A seriously great thing, and one to build on. Brilliant.

### Where it is still thin

1. **It is young.** The program was made in November 2026, with and for its curator. Nobody has completed it yet, and what it teaches has not been measured.
2. **The sources were checked against summaries, not the books.** Claude wrote the text under the curator's direction, and checked it by web search, mostly against secondary sources, on the dates the textbook gives. Dettmer's book, Goldratt's own text, Sarasvathy's 2001 paper and Klein's full article were not reached. Before you lean on a claim, read its source; and if you find an error, tell us.
3. **The tutor is an AI.** It can sound sure and be wrong, and it voices the thinkers in its own words. None of them has reviewed this. Treat what it says as something to test, which is what the program teaches anyway.
4. **Some things are still done by hand.** A new learner's start and the progress line have each been tried once, and the start by voice and the feedback note not yet at all. The voice tutor's summary is copied into the workbook by hand, and each program writes its own voice tutor.

### The small print

It has only been tried with Anthropic's Claude, and is not affiliated with Anthropic. What you tell the tutor goes to your AI provider under its terms; backing up your workbook is up to you. It is not professional advice of any kind. Before 1.0, files and formats may change.

## Contributing

Issues and pull requests are welcome. The most useful ones correct a source or report what happened when you tried a session. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md). Never put a workbook, or anyone's private case, in an issue or a pull request.

## Licence and credit

© 2026 Magnus Vestin, Keys2Collaboration. The text of this repository is licensed under [Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0). You may use it, change it and share it, also commercially, if you give credit. For example:

> keys2learning by Magnus Vestin, Keys2Collaboration, CC BY 4.0. https://github.com/the-magnus/keys2learning

The licence comes with no warranty. It covers this repository's own text. The books, papers and reports it cites belong to their authors and publishers, and the product names it mentions belong to their owners.

## Thanks

1. Sharon Bowman, for the 4Cs in *Training from the Back of the Room!*
2. The thinkers the program rests on. They are named in its [`about.md`](programs/building-with-agents-and-science/about.md).
