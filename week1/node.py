class Node:
    """
    Class which is resposible for ordering and locations for elements in cache
    """

    def __init__(self, content=None):
        self.next = None
        self.frequency = 0
        self.content = None
