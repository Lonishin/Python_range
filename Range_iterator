class Range:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step == 0:
            raise ValueError
        if self.current - self.stop ==0:
            raise StopIteration
        if abs(self.stop - self.current) <self.step:
                return self.current
        if self.step < 0 and self.current <= self.stop:
            raise StopIteration
        if self.current > self.stop and self.step > 0:
            raise StopIteration
        self.current = self.current + self.step
        return self.current - self.step
