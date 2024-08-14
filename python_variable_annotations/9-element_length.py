#!/usr/bin/env python3
"""contient la méthode element_length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Renvoie une liste de tuples contenant chaque élément de la liste
    d'entrée et sa longueur."""
    return [(i, len(i)) for i in lst]
