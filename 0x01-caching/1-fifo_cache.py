#!/usr/bin/env python3
""" 1-fifo_cache Module """

BaseCaching = __import__('base_caching').BaseCaching

        
class LIFOCache(BaseCaching):
    """
    FIFOCache class

    Implements the First-In-First-Out (FIFO) caching algorithm.
    """

    def __init__(self):
        """ Initialize the FIFOCache object """

        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Add an item to the cache

        Args:
            key: The key for the item.
            item: The value of the item.

        Return:
            Nothing, If the key or item is None,
            Otherwise, assigns item to key in cache_data dictionary.
        """

        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.stack.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            discarded_key = self.stack.pop()
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """
        Get an item from the cache

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value of key in the cache_data dictionary,
            or None if key is None or does not exist
        """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]

