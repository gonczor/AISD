from . import StructureHandler


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AVLHandler(StructureHandler):
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def get_height(self):
        if self.node:
            return self.height
        else:
            return 0

    def is_leaf(self):
        return self.height == 0

    def add_element(self, key):
        tree = self.node

        newnode = Node(key)

        if tree is None:
            self.node = newnode
            self.node.left = AVLHandler()
            self.node.right = AVLHandler()

        elif key < tree.key:
            self.node.left.add_element(key)

        elif key > tree.key:
            self.node.right.add_element(key)

        self.rebalance()

    def rebalance(self):
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_left()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rotate_right()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotate_right()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def rotate_right(self):
        # Rotate left pivoting on self
        node = self.node
        left_child = self.node.left.node
        left_right_child = left_child.right.node

        self.node = left_child
        left_child.right.node = node
        node.left.node = left_right_child

    def rotate_left(self):
        # Rotate left pivoting on self
        node = self.node
        right_child = self.node.right.node
        right_left_child = right_child.left.node

        self.node = right_child
        right_child.left.node = node
        node.right.node = right_left_child

    def update_heights(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, key):
        if self.node is not None:
            if self.node.key == key:
                if self.node.left.node is None and self.node.right.node is None:
                    self.node = None
                # if only one subtree, take that
                elif self.node.left.node is None:
                    self.node = self.node.right.node
                elif self.node.right.node is None:
                    self.node = self.node.left.node

                # worst-case: both children present. Find logical successor
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement is not None:  # sanity check
                        self.node.key = replacement.key

                        # replaced. Now delete the key from right child
                        self.node.right.delete(replacement.key)

                self.rebalance()
                return
            elif key < self.node.key:
                self.node.left.delete(key)
            elif key > self.node.key:
                self.node.right.delete(key)

            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):
        """
        Find the biggest valued node in LEFT child
        """
        node = node.left.node
        if node is not None:
            while node.right is not None:
                if node.right.node is None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        """
        Find the smallest valued node in RIGHT child
        """
        node = node.right.node
        if node is not None:

            while node.left is not None:
                if node.left.node is None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self is None or self.node is None:
            return True

        # We always need to make sure we are balanced
        self.update_heights()
        self.update_balances()
        return (abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced()

    def inorder_traverse(self):
        if self.node is None:
            return []

        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    @classmethod
    def to_string(cls):
        return 'avl'

#
# class AVLHandler(StructureHandler):
#     @classmethod
#     def find_by_value(cls, value):
#         pass
#
#     _root = None
#
#     def get_height(self, start=True, node=None):
#         """
#         Show height by going in order. Same hacks as in show_in_order method.
#         :param start: indicates whether we are starting or not. Default to True to make end-user's
#         life easier
#         :param node: current node's height
#         :returns: height of the tree
#         """
#         if start:
#             node = self._root
#
#         if not node or not node.value:
#             return 0
#
#         left_subtree_height = self.get_height(start=False, node=node.left_child)
#         right_subtree_height = self.get_height(start=False, node=node.right_child)
#         if left_subtree_height >= right_subtree_height:
#             return left_subtree_height + 1
#         else:
#             return right_subtree_height + 1
#
#     def clear(self, start=True, node=None):
#         if start:
#             node = self._root
#
#         if not node:
#             return
#
#         self.clear(start=False, node=node.left_child)
#         self.clear(start=False, node=node.right_child)
#         node.value = None
#         node = None
#         del node
#
#     def add_element(self, value):
#         if not self._root:
#             self._root = Node(value)
#         else:
#             self._find_and_place(value, self._root)
#
#     def _find_and_place(self, value, parent):
#         if value >= parent.value:
#             if not parent.right_child:
#                 parent.right_child = Node(value)
#             else:
#                 self._find_and_place(value=value, parent=parent.right_child)
#         else:
#             if not parent.left_child:
#                 parent.left_child = Node(value)
#             else:
#                 self._find_and_place(value=value, parent=parent.left_child)
#
#         parent_is_root = parent == self._root
#
#         # rebalancing
#
#         balance = self._get_balance(parent)
#         # right is heavier
#         if balance > 3:
#             if self._get_balance(parent.left_child) < -2:
#                 parent.left_child = self.right_rotate(parent.left_child)
#             parent.right_child = self.left_rotate(parent.right_child)
#         # left is heavier
#         elif balance < -3:
#             if self._get_balance(parent.right_child) > 2:
#                 parent.right_child = self.left_rotate(parent.right_child)
#             parent.left_child = self.right_rotate(parent.left_child)
#
#         if parent_is_root:
#             self._root = parent
#
#     def right_rotate(self, node):
#         print('Left rotate of: {}'.format(node.value))
#         a = node
#         b = node.left_child
#         temp = b.right_child
#         node = b
#         b.right_child = a
#         a.left_child = temp
#         return node
#
#     def left_rotate(self, node):
#         print('Right rotate of: {}'.format(node.value))
#         a = node
#         b = node.right_child
#         temp = b.left_child
#         node = b
#         b.left_child = a
#         a.right_child = temp
#         return node
#
#     def _get_balance(self, node):
#         if not node:
#             return 0
#         else:
#             return self.get_height(node=node.right_child, start=False) - \
#                    self.get_height(node=node.left_child, start=False)
#
#     @classmethod
#     def remove_element(cls, value):
#         pass
#
#     def show_in_order(self, node=None, start=True):
#         """
#         Shows bst in the inorder manner.
#         :param start: as the algorithm is recursive an I didn't want to use separate method for
#         user to begin with or to make self._root public this is a hack to tell if we are beginning.
#         :param node: currently referred node
#         """
#         if start:
#             node = self._root
#
#         if not node:
#             return
#         self.show_in_order(node.left_child, False)
#         print(node.value)
#         self.show_in_order(node.right_child, False)
#
#     def __str__(self):
#         return 'avl'
#
#     @classmethod
#     def to_string(cls):
#         return 'avl'
#
#
# class Node:
#     right_child = None
#     left_child = None
#     value = None
#
#     def __init__(self, value):
#         self.value = value
