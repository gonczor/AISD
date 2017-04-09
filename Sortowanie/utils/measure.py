import time

time_elapsed = []


def measure(call):

    def wrapper(*args):
        global time_elapsed
        start = time.time()
        returned = call(*args)
        time_elapsed.append(time.time() - start)
        return returned

    return wrapper
