#!/usr/bin/env python3
from structures.lists import ListHandler
from structures.bst import BSTHandler
from structures.avl import AVLHandler
from timer import measure


@measure
def run():
    # ListHandler.add_element(5)
    # ListHandler.add_element(4)
    # ListHandler.add_element(7)
    #
    # ListHandler.show()
    # print('###')
    # ListHandler.remove_element(7)
    #
    # ListHandler.show()
    # BSTHandler.add_element(5)
    # BSTHandler.add_element(4)
    # BSTHandler.add_element(7)
    # BSTHandler.add_element(3)
    # BSTHandler.add_element(2)
    # BSTHandler.add_element(4)
    # BSTHandler.show_in_order()
    # print('Height: {}'.format(BSTHandler.get_height()))
    # found_node = BSTHandler.find_by_value(7)
    # print('Found node: {} for value: {}'.format(found_node, found_node.value))
    # BSTHandler.clear()
    # print('Height after clear(): {}'.format(BSTHandler.get_height()))

    to_add = [0, 2, 1, 4, 3, 5, 6]
    # to_add = [1, 2, 3]

    for x in to_add:
        AVLHandler.add_element(x)

    AVLHandler.show_in_order()


if __name__ == '__main__':
    run()
