import random

from . import *


def generate_data():
    for size in SIZES:
        to_return = []
        data_file = os.path.join(DATA_DIRECTORY_NAME, str(size))

        if not os.path.exists(DATA_DIRECTORY_NAME):
            os.makedirs(DATA_DIRECTORY_NAME)

        values = [i for i in range(size)]
        max_iterations = len(values)
        for i in range(max_iterations):
            position_to_return = random.randint(0, len(values)-1)
            to_return.append(values.pop(position_to_return))

        f = open(data_file, 'w')
        for element in to_return:
            f.write('{}\n'.format(element))
        f.close()
