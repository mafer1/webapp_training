from collections import Counter, deque
from typing import NamedTuple, Union, OrderedDict


class Point(NamedTuple):
    """The Point representation in three-dimensional space"""

    x: Union[int, float] = 0.0
    y: Union[int, float] = 0.0
    z: Union[int, float] = 0.0

    def __repr__(self) -> str:
        return f"Point coordinates x:{self.x}, y:{self.y}, z:{self.z}"


class Storage:
    """Points storage"""

    def __init__(self, cache_capacity: int) -> None:
        self.storage: list[Point] = []
        self.cache = self.Cache(self.storage, cache_capacity)

    def put(self, *args):
        if isinstance(args[0], Point):
            self.storage.append(args[0])
        else:
            self.storage.append(Point(args[0], args[1], args[2]))

    def get(self, *args):
        if isinstance(args[0], Point):

            self.storage.append(args[0])
        else:
            self.storage.append(Point(args[0], args[1], args[2]))

    class Cache:
        def __init__(self, storage, capacity):
            self.capacity = capacity
            self.lru_cache = self.LRUCache(storage, capacity)
            self.lfu_cache = ...

        class LRUCache:
            def __init__(self, storage, capacity: int):
                self.storage = storage
                self.cache = OrderedDict()
                self.capacity = capacity

            def get(self, key: int) -> int:
                if key not in self.cache:
                    return -1
                else:
                    self.cache.move_to_end(key)
                    return self.cache[key]

            def put(self, key: int, value: int) -> None:
                self.cache[key] = value
                self.cache.move_to_end(key)
                if len(self.cache) > self.capacity:
                    self.cache.popitem(last=False)
