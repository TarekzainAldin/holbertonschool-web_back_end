#!/usr/bin/env python3
"""Fonction qui retourne une liste de tous les documents dans une collection"""


def list_all(mongo_collection):
    """Method to list all"""
    liste_docs_de_la_collection = []
    if mongo_collection.find():
        for data in mongo_collection.find():
            liste_docs_de_la_collection.append(data)

    return liste_docs_de_la_collection
