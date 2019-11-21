class UserFactory:
    """User factory"""

    def __init__(self):
        self._positions = {}

    def register_position(self, position, creator):
        """Add new user position"""
        self._positions[position] = creator

    def get_user(self, name, position):
        """Get user instance by position"""
        creator = self._positions.get(position.lower())
        if not creator:
            raise ValueError(position)
        return creator(name)


class User:

    def __init__(self, name):
        self.name = name

    def is_enough_rights(self):
        return True if isinstance(self, Salesman) else False


class Manager(User):
    pass


class Salesman(User):

    @staticmethod
    def add_entry(order, **kwargs):
        order.add_entry(**kwargs)


factory = UserFactory()
factory.register_position(u'salesman', Salesman)
factory.register_position(u'manager', Manager)
