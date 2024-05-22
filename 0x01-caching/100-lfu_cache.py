#!/usr/bin/env python3
""" 100-lfu_cache Module """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ An LFU cache that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the LFUCache instance """

        super().__init__()
        self.frequency = {}
        self.usage = {}

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

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self._evict()
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage[key] = 1

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

        self.usage[key] += 1
        return self.cache_data[key]

    def _evict(self):
        """ Evict the least frequently used item(s) from the cache """

        min_frequency = min(self.frequency.values())
        candidates = [
          key for key in self.frequency if self.frequency[key] == min_frequency
          ]
        lru_key = min(candidates, key=lambda k: self.usage[k])
        del self.cache_data[lru_key]
        del self.frequency[lru_key]
        del self.usage[lru_key]
        print("DISCARD: {}".format(lru_key))
