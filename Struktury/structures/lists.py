from errors import NotFoundError
from structures import StructureHandler


class ListHandler(StructureHandler):
    _my_list_head = None
    _my_list_current = None

    @classmethod
    def add_element(cls, value):
        if not cls._my_list_head:
            cls._my_list_head = Node(value)
        else:
            # Special case: current element is smaller than head
            if value < cls._my_list_head.value:
                new_head = Node(value)
                new_head.next = cls._my_list_head
                cls._my_list_head = new_head
            else:
                current_node = cls._my_list_head
                # Find place to insert. Break conditions:
                #   1. We are in the last node (next node doesn't exist)
                #   2. Next node exists and is greater than current value
                while current_node.next and current_node.next.value < value:
                    current_node = current_node.next

                tmp = current_node.next
                current_node.next = Node(value)
                current_node.next.next = tmp

    @classmethod
    def show(cls):
        tmp = cls._my_list_head
        while tmp:
            print(tmp.value)
            tmp = tmp.next

    @classmethod
    def remove_element(cls, value):
        tmp = cls._my_list_head
        previous = None

        while tmp and tmp.value != value:
            previous = tmp
            tmp = tmp.next

        if tmp:
            if tmp == cls._my_list_head:
                cls._my_list_head = cls._my_list_head.next
                del tmp
            else:
                previous.next = tmp.next
                del tmp

        else:
            raise NotFoundError

    @classmethod
    def find_by_value(cls, value):
        tmp = cls._my_list_head

        while tmp and tmp.value != value:
            tmp = tmp.next

        if tmp and tmp.value == value:
            return tmp
        else:
            raise NotFoundError

    @classmethod
    def clear(cls):
        deleted = cls._my_list_head
        cls._my_list_head = None
        while deleted:
            tmp = deleted.next
            del deleted
            deleted = tmp


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
