from collections import Counter, deque
from typing import NamedTuple, Union


class Point(NamedTuple):
    """The Point representation in three-dimensional space"""

    x: Union[int, float] = 0.0
    y: Union[int, float] = 0.0
    z: Union[int, float] = 0.0

    def __repr__(self) -> str:
        return f"Point coordinates x:{self.x}, y:{self.y}, z:{self.z}"


class Storage:
    """Points storage"""

    def put(self, *args):
        if isinstance(args[0], Point):
            self.storage.appendleft(args[0])
        else:
            self.storage.appendleft(Point(args[0], args[1], args[2]))

    def get_cordinates(self):
        return [(point.x, point.y, point.z) for point in self.storage]

    class Cache:
        def __init__(self, storage, cache_capacity) -> None:
            self.storage = storage
            self.cache_capacity = cache_capacity

        # Least recently used (LRU)
        def get_last_recent(self):
            return deque(self.storage, maxlen=self.cache_capacity)

        # Least-frequently used (LFU)
        def get_least_frequently(self):
            return Counter(self.storage).most_common(self.cache_capacity)
