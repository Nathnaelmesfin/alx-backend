#!/usr/bin/env python3
""" 4-mru_cache Module """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache Class

    Implements the MRU (Most Recently Used) caching algorithm
    """

    def __init__(self):
        """ Initialize the MRUCache object """

        super().__init__()
        self.keys = []

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

        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """
        Get an item from the cache

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value of key in the cache_data dictionary,
            or None if key is None or does not exist
        """

        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            return self.cache_data[key]
        return None
