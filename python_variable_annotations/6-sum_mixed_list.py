#!/usr/bin/env python3
"""contient la méthode sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """retourn un float qui est l'additionne d'un mixte de float et d'int
    d'une liste passée en paramètre"""
    return sum(mxd_lst)
