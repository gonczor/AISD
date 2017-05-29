#!/usr/bin/env python3
import os
import sys

from structures.lists import ListHandler
from structures.bst import BSTHandler
from structures.avl import AVLHandler
from timer import measure, time_elapsed
from utils.generator import generate_data
from utils import DATA_DIRECTORY_NAME, MEASUREMENT_DIRECTORY_NAME, SIZES


def run():

    task12()
    # task3()


def task12():
    handlers = [ListHandler, BSTHandler]

    for test_data_size in SIZES:
        for handler in handlers:
            build_times = []
            go_through_times = []
            delete_times = []

            measurement_path = os.path.join(MEASUREMENT_DIRECTORY_NAME)
            # Tasks 1 and 2
            task_1_and_2_directory = os.path.join(measurement_path, 'task12', handler.to_string())
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
            f.write('{}\n'.format(avg / 15))
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


def task3():
    handlers = [BSTHandler, AVLHandler]

    for test_data_size in SIZES:
        for handler in handlers:
            measurement_path = os.path.join(MEASUREMENT_DIRECTORY_NAME)
            # Tasks 1 and 2
            task_3_directory = os.path.join(measurement_path, 'task3')
            if not os.path.exists(task_3_directory):
                os.makedirs(task_3_directory)

            # get data from file
            path_to_data = os.path.join(DATA_DIRECTORY_NAME, str(test_data_size))
            f = open(path_to_data)
            numbers = []
            for line in f:
                numbers.append(int(line))
            f.close()

            structure = handler()

            for number in numbers:
                structure.add_element(number)

            # if isinstance(structure, AVLHandler):
            #     print('Size: {}'.format(test_data_size))
            #     structure.show_in_order()

            measurement_file = os.path.join(task_3_directory, handler.to_string())
            f = open(measurement_file, 'a')
            f.write('{},{}\n'.format(test_data_size, structure.get_height()))
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


def zadanie():
    elements = [15, 6, 18, 3, 7, 17, 4, 2, 20, 13, 19, 14]
    handler = BSTHandler()
    for element in elements:
        handler.add_element(element)

    print(handler.get_height())
    print('###')
    print(handler.get_most_left())
    print('###')
    handler.print_post_order()



if __name__ == '__main__':
    # if '--generate' in sys.argv or '-g' in sys.argv:
    #     generate_data()
    # else:
    #     run()
        # debug_avl()
    zadanie()
