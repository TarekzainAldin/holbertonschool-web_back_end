#!/usr/bin/env python3
"""contient la méthode make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Renvoie une fonction qui multiplie un flottant par le multiplicateur donné.
    Returns: Callable[[float], float]: Une fonction prenant un flottant en
    entrée et renvoyant un flottant.
    """
    def multiplier_function(x: float) -> float:
        """ Multiplie un flottant par le multiplicateur donné.
        Returns: float: Le résultat de la multiplication."""
        return x * multiplier

    return multiplier_function
