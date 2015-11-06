from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def set(self, key, value):
        #print self.index, self.cache
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.size:
            self.cache.popitem(False)
        self.cache[key] = value
