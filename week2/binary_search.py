class BinarySearch:
    """Binary search"""

    def __init__(self, value, start=0, end=100):
        self.start = start
        self.end = end
        self.value = value
        self.steps_count = 0

    def search(self):
        _range = list(range(self.start, self.end))

        while True:
            self.steps_count += 1
            if self.value < _range[len(_range) // 2]:
                _range = _range[: len(_range) // 2]

            elif self.value == _range[len(_range) // 2]:
                return self.value, self.steps_count

            else:
                _range = _range[len(_range) // 2 :]
