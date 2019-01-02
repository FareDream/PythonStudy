from types import MethodType

class MyClass(object):
    __slots__ = ['name','set_name']

def set_name(self, name):
    self.name = name


cls = MyClass()
cls.name = 'Tom'
print(cls.name)
cls.set_name = MethodType(set_name, cls)
cls.set_name('Jerry')
print(cls.name)