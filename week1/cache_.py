from typing import Deque
from collections import deque, namedtuple, Counter

Element = namedtuple("Element", ["a"])
e1= Element(1)
e2= Element(1)
e3= Element(1)
e4= Element(3)
e5= Element(3)
e6= Element(5)


list_of_es = [e1, e2, e3, e4, e5]

deque_of_es = deque(list_of_es, maxlen=4)
# most common
es = Counter(deque_of_es)
es.most_common()

# last n elements

class Cache:
    def __init__(self) -> None:
        self.elements= []
        self.max_len = 5
  
    def append_element(self, element):
        self.elements.append(element)

    def return_elements(self):
        return deque(self.elements, maxlen=self.max_len)

    def return_most_common(self):
        return Counter(self.elements)
        
cla = Cache()
cla.append_element("xD")
cla.append_element("xD")
cla.append_element("xD")
cla.append_element("xD")
cla.append_element("xD")
cla.append_element("xD")

cla.elements

c = cla.return_elements()
print(c)

if __name__ == "__main__":
	print(cla.elements)
