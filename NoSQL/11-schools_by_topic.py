#!/usr/bin/env python3
"""Contient la fonction schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """Retourne liste des écoles ayant le 'topic' passé en argument"""

    return mongo_collection.find({'topics': topic})
