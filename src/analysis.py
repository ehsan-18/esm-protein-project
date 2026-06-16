from typing import Dict
from collections import Counter
import math


def length(seq: str) -> int:
    return len(seq)


def amino_acid_counts(seq: str) -> Dict[str, int]:
    return dict(Counter(seq))


def gc_content_like_metric(seq: str) -> float:
    """
    Just a diversity proxy (bioinformatics style metric)
    """
    counts = Counter(seq)
    total = len(seq)
    return len(counts) / total


def sequence_entropy(seq: str) -> float:
    counts = Counter(seq)
    total = len(seq)

    entropy = 0
    for c in counts.values():
        p = c / total
        entropy -= p * math.log2(p)

    return entropy