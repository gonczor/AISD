import gc

from errors import NotFoundError
from structures import StructureHandler


class BSTHandler(StructureHandler):
    _root = None

    @classmethod
    def find_by_value(cls, value, node=None, start=True):
        """
        Search in order
        """
        if start:
            node = cls._root

        if not node:
            return None

        if node.value == value:
            return node

        found_node = cls.find_by_value(value=value, start=False, node=node.left_child)
        if found_node:
            return found_node
        found_node = cls.find_by_value(value=value, start=False, node=node.right_child)
        if found_node:
            return found_node
        else:
            return None

    @classmethod
    def clear(cls, start=True, node=None):
        if start:
            node = cls._root

        if not node:
            return

        cls.clear(start=False, node=node.left_child)
        cls.clear(start=False, node=node.right_child)
        node.value = None
        node = None
        del node

    @classmethod
    def remove_element(cls, value):
        pass

    @classmethod
    def add_element(cls, value):
        if not cls._root:
            cls._root = Node(value)
        else:
            cls._find_and_place(value)

    @classmethod
    def _find_and_place(cls, value):
        current_node = cls._root
        while True:
            if value > current_node.value:
                if current_node.right_child:
                    current_node = current_node.right_child
                else:
                    current_node.right_child = Node(value)
                    return
            else:
                if current_node.left_child:
                    current_node = current_node.left_child
                else:
                    current_node.left_child = Node(value)
                    return

    @classmethod
    def show_in_order(cls, node=None, start=True):
        """
        Shows bst in the inorder manner.
        :param start: as the algorithm is recursive an I didn't want to use separate method for
        user to begin with or to make self._root public this is a hack to tell if we are beginning.
        :param node: currently referred node
        """
        if start:
            node = cls._root

        if not node:
            return
        cls.show_in_order(node.left_child, False)
        print(node.value)
        cls.show_in_order(node.right_child, False)

    @classmethod
    def get_height(cls, start=True, node=None):
        """
        Show height by going in order. Same hacks as in show_in_order method.
        :param start: indicates whether we are starting or not. Default to True to make end-user's
        life easier
        :param node: current node's height
        :returns: height of the tree
        """
        if start:
            node = cls._root

        if not node or not node.value:
            return 0

        left_subtree_height = cls.get_height(start=False, node=node.left_child)
        right_subtree_height = cls.get_height(start=False, node=node.right_child)
        if left_subtree_height >= right_subtree_height:
            return left_subtree_height + 1
        else:
            return right_subtree_height + 1


class Node:
    left_child = None
    right_child = None
    value = None

    def __init__(self, value):
        self.value = value
