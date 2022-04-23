from os import preadv


class Node:
    def __init__(self, prev, next, data) -> None:
        self.prev = None
        self.next = None
        self.data = data
