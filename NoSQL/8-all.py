#!/usr/bin/env python3
"""
Lists all documents in collection
"""
def list_all(mongo_collection):
    """Lists all documents in collection"""
    return list(mongo_collection.find())
