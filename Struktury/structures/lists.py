from Struktury.errors import NotFoundError
from Struktury.structures import StructureHandler


class ListHandler(StructureHandler):
    _my_list_head = None
    _my_list_current = None

    def add_element(self, value):
        if not self._my_list_head:
            self._my_list_head = Node(value)
        else:
            # Special case: current element is smaller than head
            if value < self._my_list_head.value:
                new_head = Node(value)
                new_head.next = self._my_list_head
                self._my_list_head = new_head
            else:
                current_node = self._my_list_head
                # Find place to insert. Break conditions:
                #   1. We are in the last node (next node doesn't exist)
                #   2. Next node exists and is greater than current value
                while current_node.next and current_node.next.value < value:
                    current_node = current_node.next

                tmp = current_node.next
                current_node.next = Node(value)
                current_node.next.next = tmp

    def show(self):
        tmp = self._my_list_head
        while tmp:
            print(tmp.value)
            tmp = tmp.next

    def remove_element(self, value):
        tmp = self._my_list_head
        previous = None

        while tmp and tmp.value != value:
            previous = tmp
            tmp = tmp.next

        if tmp:
            if tmp == self._my_list_head:
                self._my_list_head = self._my_list_head.next
                del tmp
            else:
                previous.next = tmp.next
                del tmp

        else:
            raise NotFoundError

    def find_by_value(self, value):
        tmp = self._my_list_head

        while tmp and tmp.value != value:
            tmp = tmp.next

        if tmp and tmp.value == value:
            return tmp
        else:
            raise NotFoundError

    def clear(self):
        deleted = self._my_list_head
        self._my_list_head = None
        while deleted:
            tmp = deleted.next
            del deleted
            deleted = tmp

    def __str__(self):
        return 'list'


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
