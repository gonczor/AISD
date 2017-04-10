from Struktury.structures import StructureHandler


class AVLHandler(StructureHandler):
    @classmethod
    def find_by_value(cls, value):
        pass

    _root = None

    def get_height(self, start=True, node=None):
        """
        Show height by going in order. Same hacks as in show_in_order method.
        :param start: indicates whether we are starting or not. Default to True to make end-user's
        life easier
        :param node: current node's height
        :returns: height of the tree
        """
        if start:
            node = self._root

        if not node or not node.value:
            return 0

        left_subtree_height = self.get_height(start=False, node=node.left_child)
        right_subtree_height = self.get_height(start=False, node=node.right_child)
        if left_subtree_height >= right_subtree_height:
            return left_subtree_height + 1
        else:
            return right_subtree_height + 1

    def clear(self, start=True, node=None):
        if start:
            node = self._root

        if not node:
            return

        self.clear(start=False, node=node.left_child)
        self.clear(start=False, node=node.right_child)
        node.value = None
        node = None
        del node

    def add_element(self, value):
        if not self._root:
            self._root = Node(value)
        else:
            self._find_and_place(value, self._root)

    def _find_and_place(self, value, parent):
        if value >= parent.value:
            if not parent.right_child:
                parent.right_child = Node(value)
            else:
                self._find_and_place(value=value, parent=parent.right_child)
        else:
            if not parent.left_child:
                parent.left_child = Node(value)
            else:
                self._find_and_place(value=value, parent=parent.left_child)

        parent_is_root = parent == self._root

        # rebalancing

        balance = self._get_balance(parent)
        # right is heavier
        if balance > 1:
            if self._get_balance(parent.left_child) < 0:
                self.left_rotate(parent)
            parent = self.right_rotate(parent)
        # left is heavier
        elif balance < -1:
            if self._get_balance(parent.right_child) > 0:
                self.right_rotate(parent)
            parent = self.left_rotate(parent)

        if parent_is_root:
            self._root = parent

    def left_rotate(self, node):
        a = node
        b = node.left_child
        temp = b.right_child
        node = b
        b.right_child = a
        a.left_child = temp
        return node

    def right_rotate(self, node):
        a = node
        b = node.right_child
        temp = b.left_child
        node = b
        b.left_child = a
        a.right_child = temp
        return node

    def _get_balance(self, node):
        if not node:
            return 0
        else:
            return self.get_height(node=node.right_child, start=False) - \
                   self.get_height(node=node.left_child, start=False)

    @classmethod
    def remove_element(cls, value):
        pass

    def show_in_order(self, node=None, start=True):
        """
        Shows bst in the inorder manner.
        :param start: as the algorithm is recursive an I didn't want to use separate method for
        user to begin with or to make self._root public this is a hack to tell if we are beginning.
        :param node: currently referred node
        """
        if start:
            node = self._root

        if not node:
            return
        self.show_in_order(node.left_child, False)
        print(node.value)
        self.show_in_order(node.right_child, False)

    def __str__(self):
        return 'avl'


class Node:
    left_child = None
    right_child = None
    value = None

    def __init__(self, value):
        self.value = value
