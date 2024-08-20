#!/usr/bin/env python3
"""Contient la fonction index_range."""


def index_range(page, page_size):
    """Retournes un tuple de deux éléments correspondant à l'index de départ
    et l'index de fin pour une page donnée."""

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
