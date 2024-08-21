#!/usr/bin/env python3
"""Contient la fonction insert_school"""


def insert_school(mongo_collection, **kwargs):
    """Ajoute un document à une collection MongoDB"""
    InsertOneResult = mongo_collection.insert_one(kwargs)
    inserted_id = InsertOneResult.inserted_id

    return inserted_id
