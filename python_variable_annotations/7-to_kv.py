#!/usr/bin/env python3
"""contient la méthode to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """retourn un tuple avec  clé et valeur au carré passée en paramètre"""
    return (k, v * v)
