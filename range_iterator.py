class Range:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step
        self.flag = 0
        if self.step == 0:
            raise ValueError

    def __iter__(self):
        return self

    def __next__(self):
        if self.current - self.stop == 0:
            raise StopIteration
        if self.step*(self.current - self.stop) > 0:
            raise StopIteration
        if abs(self.stop - self.current) < self.step:
            if self.flag == 0 or self.flag == 2:
                raise StopIteration
            self.flag = 2
            return self.current
        self.flag = 1
        self.current += self.step
        return self.current - self.step

