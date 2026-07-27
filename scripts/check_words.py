#!/usr/bin/env python3
"""Scan files for banned AI-slop words and phrases.

Usage:
    python check_words.py file1 [file2 ...]
    python check_words.py src/            # walks a directory (.html .jsx .tsx .md .txt .js .ts .vue .svelte)

Exit code 1 when hits are found, so it can gate CI.
Core list embedded below; the full annotated list lives in references/banned-words.md.
"""
import re
import sys
from pathlib import Path

WORDS = """
delve delves delving embark elevate elevates empower empowers unleash unlock
harness leverage leverages utilize utilizes foster fosters bolster garner
streamline streamlines supercharge turbocharge skyrocket revolutionize
transformative redefine reimagine disrupt orchestrate
underscore underpin spearhead propel catalyze galvanize demystify captivate
resonate transcend amplify optimize maximize facilitate curate hone
future-proof surpass boast boasts
robust seamless seamlessly effortless effortlessly frictionless cutting-edge
state-of-the-art groundbreaking game-changing game-changer innovative
next-gen next-generation best-in-class world-class top-notch unparalleled
unprecedented unrivaled unmatched bespoke holistic immersive intuitive
sleek stunning breathtaking dazzling meticulous pivotal crucial paramount
invaluable indispensable actionable scalable turnkey plug-and-play
mission-critical visionary compelling captivating exquisite flawless
pixel-perfect hassle-free laser-focused lightning-fast blazing-fast
buttery-smooth silky-smooth intricate multifaceted ever-evolving
ever-changing fast-paced unwavering relentless boundless limitless
landscape realm tapestry testament cornerstone powerhouse synergy paradigm
plethora myriad symphony beacon catalyst linchpin bedrock epitome pinnacle
zenith culmination nexus frontier
furthermore moreover additionally consequently subsequently essentially
ultimately notably undoubtedly undeniably
""".split()

PHRASES = [
    "in today's digital age", "in today's fast-paced", "in the fast-paced world",
    "in an era where", "it's worth noting", "it's important to note",
    "look no further", "we've got you covered", "to the next level",
    "elevate your", "unlock the power", "unlock the secrets",
    "unlock the potential", "embark on a journey", "navigate the complexities",
    "a testament to", "stands as", "serves as", "say goodbye to",
    "the future of", "welcome to the future", "revolutionize the way",
    "supercharge your", "but that's not all", "here's the kicker",
    "let's face it", "picture this", "imagine a world", "gone are the days",
    "more than just", "one-stop shop", "trusted by thousands",
    "join thousands of", "made with love", "whether you're a",
    "game changer", "deep dive", "treasure trove", "secret sauce",
    "north star", "paradigm shift", "at the end of the day",
    "when it comes to", "first and foremost", "last but not least",
    "in conclusion", "needless to say", "seamlessly integrates",
]

EXTS = {".html", ".htm", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte", ".md", ".txt", ".mdx"}
WORD_RE = re.compile(r"\b(" + "|".join(re.escape(w) for w in WORDS) + r")\b", re.IGNORECASE)
PHRASE_RE = re.compile("|".join(re.escape(p) for p in PHRASES), re.IGNORECASE)


def gather(paths):
    for p in paths:
        p = Path(p)
        if p.is_dir():
            yield from (f for f in p.rglob("*") if f.suffix.lower() in EXTS)
        elif p.is_file():
            yield p


def main(argv):
    if not argv:
        print(__doc__)
        return 0
    hits = 0
    for f in gather(argv):
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if "banned-words" in f.name or "check_words" in f.name:
            continue  # skip the list and this script
        for n, line in enumerate(text.splitlines(), 1):
            found = [m.group(0) for m in WORD_RE.finditer(line)]
            found += [m.group(0) for m in PHRASE_RE.finditer(line)]
            for term in found:
                hits += 1
                print(f"{f}:{n}: {term!r}  ->  {line.strip()[:90]}")
    if hits:
        print(f"\n{hits} hit(s). Replace with plain words, or justify in the slop-test record.")
        return 1
    print("Clean: no banned words or phrases found.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
