
def init(self,name):
    self.name = name
def say_hello(self):
    print("Hello, %s!" % self.name)
# 使用type 动态创建类
Hello = type('Hello', (object,), dict(__init__ = init, hello = say_hello))
h = Hello('Tom')
h.hello()

print('--------------------------------------------------------')

class MateClass(type):
    def __new__(cls, name, bases, attrs):
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        attrs['a'] = lambda self , value : self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=MateClass):
    pass

mli = MyList()
mli.a(1)
mli.a(1)
mli.a(1)
print(mli)
print('--------------------------------------------------------')
