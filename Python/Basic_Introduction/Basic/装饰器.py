from functools import wraps

def hello(fn):
    # 如果不加此注解结果为
    # hellofoo
    # i am foo
    # goodbyefoo
    # wrapper
    @wraps(fn)
    def wrapper():
        print('hello' + fn.__name__)
        fn()
        print('goodbye' + fn.__name__)
    return wrapper

@hello
def foo():
    print('i am foo')

foo()
print(foo.__name__)
#现在的结果为
# hellofoo
# i am foo
# goodbyefoo
# foo