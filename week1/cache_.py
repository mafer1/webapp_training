from typing import Deque
from collections import deque, namedtuple, Counter

Element = namedtuple("Element", ["a"])

list_elements = [
    Element(1),
    Element(1),
    Element(1),
    Element(3),
    Element(3),
    Element(5),
]

def return_last_elements(elements_list: list, num_of_element: int=5):
    return deque(elements_list, maxlen=num_of_element)


def return_most_common_elements(elements_list: list, most_common_num: int=1):
    return Counter(elements_list).most_common(most_common_num)


if __name__ == "__main__":
    print(f"Most common elements: {return_most_common_elements(list_elements, 2)}")
    print(f"Most recent elements: {return_last_elements(list_elements, 2)}")
