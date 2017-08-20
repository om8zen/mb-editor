from mb_editor.implicit import Implicit


class Field:

    def __init__(self, key, value, type):
        self.key = key

        self.implicit_default = None
        self.type = value.type if type == Implicit else type

        self.value = value

    def __repr__(self):
        return '{} = "{}";'.format(self.key, self.value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) == Implicit:
            self.type = value.type
            self._value = value.type(value.value)
            self.implicit_default = self._value
        else:
            self._value = self.type(value)

    def is_explicit(self):
        return (
            (self.value is not None and self.implicit_default is None)
            or (self.value is None and self.implicit_default is not None)
            or self.value != self.implicit_default
        )


    @staticmethod
    def tests():
        f = Field("name", "EdBeacham", str)
        assert (f.key, f.value, f.type) == ("name", "EdBeacham", str)

        from mb_editor.numberlists.vector3d import Vector3D
        f.key, f.type, f.value = "areaCode", Vector3D, [2, 1, 4]
        assert f.value == "2 1 4"

        from mb_editor.objectname import ObjectName
        f.key, f.type, f.value = "client", ObjectName, "RichardSwiney"
        from mb_editor.scriptobject import ScriptObject
        assert f.value == ScriptObject("RichardSwiney")

        g = Field("timeBonus", Implicit(5000), Implicit)
        assert (g.value, g.type, g.implicit_default) == (5000, int, 5000)

        g.value = Implicit(3000)
        assert (g.value, g.type, g.implicit_default) == (3000, int, 3000)

        g.value = 1000
        assert (g.value, g.type, g.implicit_default) == (1000, int, 3000)


if __name__ == '__main__':
    Field.tests()
