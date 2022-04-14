from typing import NamedTuple, Union


class Point(NamedTuple):
    """The Point representation in three-dimensional space"""

    x: Union[int, float] = 0.0
    y: Union[int, float] = 0.0
    z: Union[int, float] = 0.0

    def __repr__(self) -> str:
        return f"Point coordinates x:{self.x}, y:{self.y}, z:{self.z}"

class Storage:
    ...