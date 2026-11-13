"""Build each program as one file, for a release.

A learner away from the desk needs a Claude Project holding the program's
about.md and textbook.md and programs/tutoring.md, and a few sentences that
tell the model it is the tutor. This writes them as one file per program,
dist/<program>.md, to attach to a GitHub release, so the learner downloads
one file. dist/ is not in git: the file is built from the sources at
release time and never edited.

Usage, from the repository's root:
    python3 development/bundle.py
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

INSTRUCTIONS = (
    'To the AI model reading this file in a project: you are the learner\'s tutor in the program '
    '"{title}". This file holds the program in three parts: tutoring.md, about.md and '
    "textbook.md. Read tutoring.md first: it "
    "says what you are for. The learner's own record is workbook.md; if the project holds none, "
    'they are new, so start them off as "First session" in tutoring.md says.'
)


def version():
    """The newest released version in CHANGELOG.md."""
    found = re.search(r"^## \[(\d+\.\d+(?:\.\d+)?)\]", (ROOT / "CHANGELOG.md").read_text(), re.M)
    if not found:
        sys.exit("no released version found in CHANGELOG.md")
    return found.group(1)


def bundle(program):
    """The single file's text for one program folder."""
    title = (program / "about.md").read_text().splitlines()[0].lstrip("# ").strip()
    parts = [
        f"# {title}",
        f"keys2learning {version()}. Built from the repository's files; do not edit. "
        "https://github.com/the-magnus/keys2learning",
        INSTRUCTIONS.format(title=title),
        "## How to set up\n"
        "1. Create a Claude Project and add this file to the Project's own files, not to a chat.\n"
        "2. Paste this sentence into the Project's instructions: \"You are my tutor. Before your "
        f"first reply in every conversation, read the file {program.name}.md in this project, and my "
        "workbook.md if there is one, and follow the file's part tutoring.md.\"\n"
        "3. Start a conversation, by voice or text, and say hello. The tutor saves your workbook "
        "to the Project where it can; where it can't, it tells you what to save as workbook.md "
        "and add to the Project.",
    ]
    for name, path in (("tutoring.md", ROOT / "programs" / "tutoring.md"),
                       ("about.md", program / "about.md"),
                       ("textbook.md", program / "textbook.md")):
        parts.append(f"## File: {name}\n" + path.read_text().strip())
    return "\n\n".join(parts) + "\n"


def main():
    out = ROOT / "dist"
    out.mkdir(exist_ok=True)
    programs = sorted(p.parent for p in (ROOT / "programs").glob("*/textbook.md"))
    if not programs:
        sys.exit("no program with a textbook.md found")
    for program in programs:
        target = out / f"{program.name}.md"
        target.write_text(bundle(program))
        print(f"wrote {target.relative_to(ROOT)} ({len(target.read_text().split())} words)")


if __name__ == "__main__":
    main()
