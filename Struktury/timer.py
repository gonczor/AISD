import time


def measure(runner_function):
    def wrapper():

        start = time.time()
        runner_function()
        print(time.time() - start)

    return wrapper
