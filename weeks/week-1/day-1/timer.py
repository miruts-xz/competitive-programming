import datetime as dt


class Timer:
    """
    Maintains a timer to measure running times of algorithms

    """

    def __init__(self):
        self.start = dt.datetime.now()

    def stop(self):
        return dt.datetime.now() - self.start
