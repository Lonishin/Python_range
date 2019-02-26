class GenRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        if self.step == 0:
            raise ValueError
        if self.step > 0:
            while self.start < self.stop:
                yield self.start
                self.start = self.start + self.step
        else:
            while self.start > self.stop:
                yield self.start
                self.start = self.start + self.step
