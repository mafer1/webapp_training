
class Node:
    """
    Class which is resposible for ordering and locations for elements in cache
    """

    def __init__(self, content=None):
        self.content = content
        self.next = None


class LFUCache:
    """
    Least frequently used: store elements which are frequently used (index how often are used). Element which has least
    number of usage and is the oldest are deleted from Storage and replaced by the newest one.
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def put(self, content):
        if not self.head:
            self.head = Node(content)
        else:
            last_data = self.head
            while last_data.next:
                last_data = last_data.next
            else:
                last_data.next = Node(content)

    def _count_elements(self):
        ...



    def get(self):
        ...
