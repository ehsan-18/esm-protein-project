from typing import Dict, List
import math
from collections import Counter


AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"


def validate_sequence(seq: str) -> None:
    if not seq:
        raise ValueError("Empty sequence")
    if any(aa not in AMINO_ACIDS for aa in seq):
        raise ValueError("Invalid amino acid detected")


def amino_acid_composition(seq: str) -> Dict[str, float]:
    """
    Fractional composition of amino acids
    """
    validate_sequence(seq)
    length = len(seq)
    counts = Counter(seq)
    return {aa: counts.get(aa, 0) / length for aa in AMINO_ACIDS}


def shannon_entropy(seq: str) -> float:
    """
    Sequence complexity (information content)
    """
    validate_sequence(seq)
    counts = Counter(seq)
    length = len(seq)

    entropy = 0.0
    for c in counts.values():
        p = c / length
        entropy -= p * math.log2(p)

    return entropy


# Kyte-Doolittle scale (hydrophobicity)
HYDRO_SCALE = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5,
    "C": 2.5, "Q": -3.5, "E": -3.5, "G": -0.4,
    "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9,
    "M": 1.9, "F": 2.8, "P": -1.6, "S": -0.8,
    "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2
}


def hydrophobicity_profile(seq: str) -> float:
    validate_sequence(seq)
    return sum(HYDRO_SCALE.get(aa, 0) for aa in seq) / len(seq)


def esm_embedding_placeholder(seq: str):
    """
    This will be used in Colab with fair-esm model
    """
    return {
        "sequence_length": len(seq),
        "note": "Use ESM model in Colab to generate real embeddings"
    }