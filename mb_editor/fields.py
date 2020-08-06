from mb_editor.field import Field


class Fields:
    def __init__(self, fields_list=None):
        self.list = [] if fields_list is None else fields_list

    def __repr__(self):
        return '\n'.join(map(repr, filter(lambda field: field.is_explicit(), self.list)))

    @property
    def dict(self):
        return {
            field.key: field.value for field in self.list
        }

    def field_with_key(self, key):
        return next(filter(lambda field: field.key == key, self.list), None)

    def get(self, key):
        try:
            return self.field_with_key(key).value
        except AttributeError:
            return None

    def set(self, key, value, field_type=None):
        if '.' in key:
            before_dot, after_dot = tuple(key.split('.', 1))
            self.get(before_dot).__setattr__(after_dot, value)
            return

        try:
            self.field_with_key(key).value = value
        except AttributeError:
            self.list.append(Field(key, value, type(value) if field_type is None else field_type))

    def delete(self, key):
        try:
            self.list.remove(self.field_with_key(key))
        except AttributeError:
            pass
