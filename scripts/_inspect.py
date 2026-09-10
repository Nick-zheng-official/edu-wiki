# -*- coding: utf-8 -*-
# Temporary mechanical helper: verify article word count + vocab coverage. Safe to delete.
import re

art = open(r"d:\edu-wiki\scripts\_article4.txt", encoding="utf-8").read()
words = [w.strip().replace('_', ' ') for w in open(r"d:\edu-wiki\scripts\export-vocabs.txt", encoding="utf-8")]

# word count: hyphenated words count as one; title excluded? include body only (drop title line)
lines = [l for l in art.strip().split("\n") if l.strip()]
body = " ".join(lines[1:])
wc = len(re.findall(r"[A-Za-z][A-Za-z'\-]*", body))
print("BODY WORD COUNT (excl. title):", wc)
print("TITLE:", lines[0])

low = art.lower()

targets = ["rainbow","shower","Celsius","temperature","peak","ridge","slope","overlook",
"southern","southeast","southwest","northeast","northwest","eastern","oriental",
"inevitable","irreversible","irregularly","inappropriate","abnormal",
"sediment","silt","muddy","clay","rural","suburb","outskirts","remote","desolate",
"distant","adjacent","pollution","pollutant","contaminate","geology","border",
"fringe","debris","crack","splendid","magnificent","super","dramatic","wilderness",
"deforest","barren","fertile","fertilize","lunar","calendar","sunrise","sunset",
"eclipse","dusk","heaven","paradise","grand","interesting","dirt","plate","mount"]

def found(w):
    wl = w.lower()
    # exact word/phrase, allow inflections for verbs/adjs (suffix up to 5 chars)
    pat = r'(?<![a-z])' + re.escape(wl) + r'(?![a-z])'
    if re.search(pat, low):
        return True
    # inflected: stem + common suffix
    for suf in ["s","es","ed","ing","d","ly","er","est","ies","ied","ation","tion","ment","ness","ity","ous","ive","al"]:
        if wl.endswith(suf) and len(wl) - len(suf) >= 4:
            stem = wl[:-len(suf)]
            if re.search(r'(?<![a-z])' + re.escape(stem) + r'[a-z]{0,5}(?![a-z])', low):
                return True
    # headword is base (e.g. deforest -> deforested): try adding suffixes
    for suf in ["s","es","ed","ing","d","ly","ies","ied","ation","tion","ment","ness","ity","ous","ive","al","er","est"]:
        if re.search(r'(?<![a-z])' + re.escape(wl) + re.escape(suf) + r'(?![a-z])', low):
            return True
    return False

missing = [w for w in targets if not found(w)]
print("\nTARGET (previously uncovered) words:", len(targets), " MISSING:", missing)

cov = [w for w in words if found(w)]
print("EXPORT WORDS COVERED BY ARTICLE 4:", len(cov), "/", len(words))
notcov = [w for w in words if not found(w)]
print("Not in article 4 (covered by art1-3 already):", len(notcov))
print(notcov)
