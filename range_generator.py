class GenRange:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step
        if self.step == 0:
            raise ValueError

    def __iter__(self):
        if self.step > 0:
            while self.current < self.stop:
                yield self.current
                self.current += self.step
        else:
            while self.current > self.stop:
                yield self.current
                self.current += self.step
