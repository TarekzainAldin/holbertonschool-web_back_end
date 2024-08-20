#!/usr/bin/env python3
"""search file for pages of data"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """Retournes un tuple de deux éléments correspondant à l'index de départ
    et l'index de fin pour une page donnée."""

    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"
    # Pour essai en pas à pas : DATA_FILE =
    "/root/holbertonschool-web_back_end/pagination/Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                # créé une listes des lignes du fichier csv
                dataset = [row for row in reader]
            # attribut à __dataset toutes les données de dataset sauf
            # la première (les entêtes de colonnes)
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get a page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, stop = index_range(page, page_size)
        dataset = self.dataset()

        # si nombre de lignes est inférieur à start, retourne une liste vide"
        if len(dataset) <= start:
            return []

        return dataset[start:stop]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """renvoie un dictionnaire contenant les valeurs suivantes :
        page_size, page, data, next_page, prev_page et total_pages"""

        a_page = self.get_page(page, page_size)

        # math.ceil() arrondir un nombre décimal à l'entier supérieur
        total_pages = (len(self.__dataset) + page_size - 1) // page_size

        return {
            "page_size": len(a_page),
            "page": page,
            "data": a_page,
            "next_page": (page + 1) if page < total_pages else None,
            "prev_page": (page - 1) if page > 1 else None,
            "total_pages": total_pages
        }
