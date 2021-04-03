

class Class:

    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = ['class %s:' % self.name]
        if self.fields:
            lines.append("   def __init__(self):")
            for field in self.fields:
                lines.append("        %s" % field)
        else:
            lines.append("   pass")
        return "\n".join(lines)


class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return 'self.%s = %s' % (self.name, self.value)


class CodeBuilder:
    def __init__(self, root_name):
        self.klass = Class(root_name)

    def add_field(self, type, name):
        self.klass.fields.append(Field(type, name))
        return self

    def __str__(self):
        return str(self.klass)


if __name__ == '__main__':
    cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
    print(cb)
