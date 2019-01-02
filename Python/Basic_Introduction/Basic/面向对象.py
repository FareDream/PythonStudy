class Fuck:
    name = "123"
    # self 指代他自己的类本身例如调用全局变量(self 可以替换为其他的变量)
    def hello(self,name):

        print(self.name)
        print(name)
obj = Fuck()
obj.hello(1)
