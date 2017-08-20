class ObjectName:

    def __init__(self, arg):
        if isinstance(arg, str):
            self._name = arg
        else:
            self._name = arg.name

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        try:
            return self.name == other.name
        except AttributeError:
            return self.name == other

ObjectName.none = ObjectName("")
