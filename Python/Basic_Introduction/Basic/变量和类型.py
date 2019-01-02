import string
def function(a,v,c):
    print(a,v,c)
class MyClass(object):
    pass
print(type(1234))
print(type(1234.123))
print(type(123.))
print(type('1234'))
print(type([1,2,    3,'1','2']))
print(type((1,'1')))
print(type(set(['1','2',3])))
print(type({'a':1,'b ':2}))
print(type(function))
print(type(string))
print(type(MyClass))

# 去除空格
str = ' 1 1 1 1 1 '
print(str)
print(str.strip())  # 两侧空格
print(str.lstrip()) # 左侧空格
print(str.rstrip()) # 右侧空格

# 字符串连接
s1 = "abc"
s2 = "DEF"
print(s1 + s2)

# 大小写转换
print(s1.upper())
print(s2.lower())
print((s1+s2).capitalize())

#位置比较
