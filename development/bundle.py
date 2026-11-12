"""Build the voice file of each program, for a release.

A learner who tutors by voice needs a Claude Project holding the program's
about.md and textbook.md and programs/tutoring.md, with voice_tutor.md's
text as its instructions. This writes them as one file per program,
dist/<program>-voice.md, to attach to a GitHub release, so the learner
downloads one file. dist/ is not in git: the file is built from the
sources at release time and never edited.

Usage, from the repository's root:
    python3 development/bundle.py
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RULE = "\n---\n"


def version():
    """The newest released version in CHANGELOG.md."""
    found = re.search(r"^## \[(\d+\.\d+\.\d+)\]", (ROOT / "CHANGELOG.md").read_text(), re.M)
    if not found:
        sys.exit("no released version found in CHANGELOG.md")
    return found.group(1)


def bundle(program):
    """The voice file's text for one program folder."""
    voice = (program / "voice_tutor.md").read_text()
    if RULE not in voice:
        sys.exit(f"{program.name}/voice_tutor.md has no --- line above its instructions")
    instructions = voice.split(RULE, 1)[1].strip()
    title = (program / "about.md").read_text().splitlines()[0].lstrip("# ").strip()
    parts = [
        f"# {title}: the voice file",
        f"keys2learning {version()}. Built from the repository's files; do not edit. "
        "https://github.com/the-magnus/keys2learning",
        "## How to set up\n"
        "1. Create a Claude Project and add this file to it.\n"
        "2. Copy the part below headed \"Instructions to paste\" into the Project's instructions.\n"
        "3. Start a voice conversation and say hello. The tutor starts you off and, at the end, "
        "says the opening of your workbook: save it as workbook.md and add it to the Project.",
        "## Instructions to paste\n" + instructions + "\n\n(The instructions to paste end here.)",
    ]
    for name, path in (("about.md", program / "about.md"),
                       ("textbook.md", program / "textbook.md"),
                       ("tutoring.md", ROOT / "programs" / "tutoring.md")):
        parts.append(f"## File: {name}\n" + path.read_text().strip())
    return "\n\n".join(parts) + "\n"


def main():
    out = ROOT / "dist"
    out.mkdir(exist_ok=True)
    programs = sorted(p.parent for p in (ROOT / "programs").glob("*/voice_tutor.md"))
    if not programs:
        sys.exit("no program with a voice_tutor.md found")
    for program in programs:
        target = out / f"{program.name}-voice.md"
        target.write_text(bundle(program))
        print(f"wrote {target.relative_to(ROOT)} ({len(target.read_text().split())} words)")


if __name__ == "__main__":
    main()
