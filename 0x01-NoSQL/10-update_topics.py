#!/usr/bin/env python3
""" 10-update_topics.py """


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name """
    if mongo_collection is not None:
        return mongo_collection.update_many(
            {"name": name}, 
            {"$set": {"topics": topics}}
            )
