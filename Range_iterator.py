class Range:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step
        if self.step == 0:
            raise ValueError

    def __iter__(self):
        return self

    def __next__(self):
        if self.current - self.stop == 0:
            raise StopIteration
        if abs(self.stop - self.current) < self.step:
            return self.current
        if self.step*(self.current - self.stop) > 0:
            raise StopIteration
        self.current += self.step
        return self.current - self.step
