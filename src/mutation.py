import random
from typing import List, Tuple


AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"


def validate(seq: str):
    if not seq:
        raise ValueError("Empty sequence")


def point_mutation(seq: str, pos: int, aa: str) -> str:
    validate(seq)

    if aa not in AMINO_ACIDS:
        raise ValueError("Invalid amino acid")

    if pos < 0 or pos >= len(seq):
        raise IndexError("Position out of range")

    return seq[:pos] + aa + seq[pos + 1:]


def generate_mutant_library(seq: str, n: int = 10) -> List[str]:
    """
    Generate random mutant sequences
    """
    validate(seq)

    mutants = []
    for _ in range(n):
        pos = random.randint(0, len(seq) - 1)
        aa = random.choice(AMINO_ACIDS)
        mutants.append(point_mutation(seq, pos, aa))

    return mutants


def systematic_scan(seq: str, position: int) -> List[Tuple[str, str]]:
    """
    Replace one position with all amino acids (classic mutagenesis scan)
    """
    validate(seq)

    results = []
    for aa in AMINO_ACIDS:
        mutated = point_mutation(seq, position, aa)
        results.append((aa, mutated))

    return results


def mutation_distance(seq1: str, seq2: str) -> int:
    if len(seq1) != len(seq2):
        raise ValueError("Length mismatch")

    return sum(a != b for a, b in zip(seq1, seq2))