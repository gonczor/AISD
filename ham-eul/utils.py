import time

duration = []


def timer(func):
    def _timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration.append(end-start)
        return result
