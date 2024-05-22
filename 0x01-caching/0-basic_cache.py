#!/usr/bin/env python3
""" 0-basic_cache Module """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class

    A caching system that inherits from the BaseCaching class.
    """

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

    def get(self, key):
        """
        Get an item from the cache

        Args:
            key: The key of item to retrieve.

        Returns:
            The key value in the cache_data dictionary,
            or None if the key is None or does not exist
        """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
