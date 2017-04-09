from structures import StructureHandler


class AVLHandler(StructureHandler):
    _root = None

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
    def add_element(cls, value):
        if not cls._root:
            cls._root = Node(value)
        else:
            cls._find_and_place(value, cls._root)

    @classmethod
    def _find_and_place(cls, value, parent):
        if value >= parent.value:
            if not parent.right_child:
                parent.right_child = Node(value)
            else:
                cls._find_and_place(value=value, parent=parent.right_child)
        else:
            if not parent.left_child:
                parent.left_child = Node(value)
            else:
                cls._find_and_place(value=value, parent=parent.left_child)

        parent_is_root = parent == cls._root

        # rebalancing

        balance = cls._get_balance(parent)
        # right is heavier
        if balance > 1:
            if cls._get_balance(parent.left_child) < 0:
                cls.left_rotate(parent)
            parent = cls.right_rotate(parent)
        # left is heavier
        elif balance < -1:
            if cls._get_balance(parent.right_child) > 0:
                cls.right_rotate(parent)
            parent = cls.left_rotate(parent)

        if parent_is_root:
            cls._root = parent

    @classmethod
    def left_rotate(cls, node):
        a = node
        b = node.left_child
        temp = b.right_child
        node = b
        b.right_child = a
        a.left_child = temp
        return node

    @classmethod
    def right_rotate(cls, node):
        a = node
        b = node.right_child
        temp = b.left_child
        node = b
        b.left_child = a
        a.right_child = temp
        return node

    @classmethod
    def _get_balance(cls, node):
        if not node:
            return 0
        else:
            return cls.get_height(node=node.right_child, start=False) -\
                   cls.get_height(node=node.left_child, start=False)

    @classmethod
    def remove_element(cls, value):
        pass

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


class Node:
    left_child = None
    right_child = None
    value = None

    def __init__(self, value):
        self.value = value
