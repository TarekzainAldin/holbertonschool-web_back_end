#!/usr/bin/env python3
"""normal commit """


def update_topics(mongo_collection, name, topics):
    """update the args  'name'"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
