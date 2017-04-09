import random
import os

from common import *


def generate_data():
    for data_type in data_types:
        directory = os.path.join(data_directory_name, data_type)
        if 'ascending' in data_type:
            generate_ascending(directory)
        elif 'descending' in data_type:
            generate_descending(directory)
        elif 'random' in data_type:
            generate_random(directory)
        elif 'constant' in data_type:
            generate_constant(directory)
        elif 'v-shaped' in data_type:
            generate_v_shaped(directory)


def generate_ascending(data_type_path):
    for size in list_sizes:
        data_storage_path = os.path.join(data_type_path, str(size))
        for probe in range(test_points_number):
            if not os.path.exists(data_storage_path):
                os.makedirs(data_storage_path)
            f = open(os.path.join(data_storage_path, str(probe)), 'w')
            for i in range(size):
                lower_boundary = i
                random_number = random.randint(lower_boundary, lower_boundary + 5)
                f.write('{}\n'.format(random_number))
            f.close()


def generate_descending(data_type_path):
    for size in list_sizes:
        data_storage_path = os.path.join(data_type_path, str(size))
        for probe in range(test_points_number):
            if not os.path.exists(data_storage_path):
                os.makedirs(data_storage_path)
            f = open(os.path.join(data_storage_path, str(probe)), 'w')
            for i in range(size):
                lower_boundary = i
                random_number = random.randint(size - lower_boundary, size - lower_boundary + 5)
                f.write('{}\n'.format(random_number))
            f.close()


def generate_random(data_type_path):
    for size in list_sizes:
        data_storage_path = os.path.join(data_type_path, str(size))
        for probe in range(test_points_number):
            if not os.path.exists(data_storage_path):
                os.makedirs(data_storage_path)
            f = open(os.path.join(data_storage_path, str(probe)), 'w')
            for i in range(size):
                random_number = random.randint(0, size)
                f.write('{}\n'.format(random_number))
            f.close()


def generate_constant(data_type_path):
    for size in list_sizes:
        data_storage_path = os.path.join(data_type_path, str(size))
        for probe in range(test_points_number):
            if not os.path.exists(data_storage_path):
                os.makedirs(data_storage_path)
            f = open(os.path.join(data_storage_path, str(probe)), 'w')
            for i in range(size):
                random_number = random.randint(size // 2 - 5, size // 2 + 5)
                f.write('{}\n'.format(random_number))
            f.close()


def generate_v_shaped(data_type_path):
    for size in list_sizes:
        data_storage_path = os.path.join(data_type_path, str(size))
        for probe in range(test_points_number):
            if not os.path.exists(data_storage_path):
                os.makedirs(data_storage_path)
            f = open(os.path.join(data_storage_path, str(probe)), 'w')
            for i in range(size):
                if i < size // 2:
                    lower_boundary = size // 2 - i
                    random_number = random.randint(lower_boundary, lower_boundary + 5)
                else:
                    lower_boundary = i - size // 2
                    random_number = random.randint(lower_boundary, lower_boundary + 5)
                f.write('{}\n'.format(random_number))
            f.close()
