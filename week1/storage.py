from typing import NamedTuple, Union


class Point(NamedTuple):
    """The Point representation in three-dimensional space"""

    x: Union[int, float] = 0.0
    y: Union[int, float] = 0.0
    z: Union[int, float] = 0.0


class Storage:
    """Points storage"""

    def __init__(self, cache_capacity: int) -> None:
        self.storage: list[Point] = []
