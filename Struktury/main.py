#!/usr/bin/env python3
import os
import sys

from Struktury.structures.lists import ListHandler
from Struktury.structures.bst import BSTHandler
from Struktury.structures.avl import AVLHandler
from Struktury.timer import measure, time_elapsed
from Struktury.utils.generator import generate_data
from Struktury.utils import DATA_DIRECTORY_NAME, MEASUREMENT_DIRECTORY_NAME, SIZES


def run():
    build_times = []
    go_through_times = []
    delete_times = []

    handlers = [ListHandler, BSTHandler]

    for test_data_size in SIZES:
        for handler in handlers:
            measurement_path = os.path.join(MEASUREMENT_DIRECTORY_NAME)
            # Tasks 1 and 2
            task_1_and_2_directory = os.path.join(measurement_path, 'task12', str(handler))
            if not os.path.exists(task_1_and_2_directory):
                os.makedirs(task_1_and_2_directory)

            build_measurement_file = os.path.join(task_1_and_2_directory, 'build')
            go_through_measurement_file = os.path.join(task_1_and_2_directory, 'go_through')
            delete_measurement_file = os.path.join(task_1_and_2_directory, 'delete')

            for test_repetition in range(1, 16):

                # get data from file
                path_to_data = os.path.join(DATA_DIRECTORY_NAME, str(test_data_size))
                f = open(path_to_data)
                numbers = []
                for line in f:
                    numbers.append(int(line))
                f.close()

                # actual testing

                structure = handler()

                # test creation
                build(structure, numbers)
                build_times.append(time_elapsed.pop())

                # test going through
                go_through_elements(structure, numbers)
                go_through_times.append(time_elapsed.pop())

                # test delete
                delete(structure)
                delete_times.append(time_elapsed.pop())

            # save results
            avg = 0.0
            for t in build_times:
                avg += t
            f = open(build_measurement_file, 'a')
            f.write('{}\n'.format(avg/15))
            f.close()

            avg = 0.0
            for t in go_through_times:
                avg += t
            f = open(go_through_measurement_file, 'a')
            f.write('{}\n'.format(avg / 15))
            f.close()

            avg = 0.0
            for t in delete_times:
                avg += t
            f = open(delete_measurement_file, 'a')
            f.write('{}\n'.format(avg / 15))
            f.close()

    # Task 3
    handlers = [BSTHandler, AVLHandler]

    for test_data_size in SIZES:
        for handler in handlers:
            measurement_path = os.path.join(MEASUREMENT_DIRECTORY_NAME)
            # Tasks 1 and 2
            task_3_directory = os.path.join(measurement_path, 'task3')
            if not os.path.exists(task_1_and_2_directory):
                os.makedirs(task_1_and_2_directory)

            # get data from file
            path_to_data = os.path.join(DATA_DIRECTORY_NAME, str(test_data_size))
            f = open(path_to_data)
            numbers = []
            for line in f:
                numbers.append(int(line))
            f.close()

            structure = handler()

            for number in numbers:
                structure.add_item(number)

            measurement_file = os.path.join(task_3_directory, str(handler))
            f = open(measurement_file, 'a')
            f.write('{},{}'.format(test_data_size, structure.get_height()))
            f.close()


@measure
def build(structure, data):
    for number in data:
        structure.add_element(number)


@measure
def delete(structure):
    structure.clear()


@measure
def go_through_elements(structure, data):
    for number in data:
        structure.find_by_value(number)


if __name__ == '__main__':
    if '--generate' in sys.argv or '-g' in sys.argv:
        generate_data()
    else:
        run()
