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
