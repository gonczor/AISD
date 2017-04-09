class StructureHandler:
    @classmethod
    def add_element(cls, value):
        raise NotImplementedError

    @classmethod
    def clear(cls):
        raise NotImplementedError

    @classmethod
    def remove_element(cls, value):
        raise NotImplementedError

    @classmethod
    def find_by_value(cls, value):
        raise NotImplementedError
