# x = 10 
# y = 20
# z = 10+20
# print(type(z))
# a = "Hello "
# b = "World"
# print(type(a+b))
class MyClass:
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __repr__(self):
        return "Call from repr " + "<%s object at %r>" % (self.__class__.__name__, hex(id(self)))
    def __eq__(self,other):
        if isinstance(other,MyClass):
            return self.x == other.x and self.y == other.y
        return False
    def __sub__(self,other):
        if isinstance(other,MyClass):
            return MyClass(self.x - other.x, self.y - other.y)
        return "Not MyClass objects"
    def __rsub__(self,other):
        return other-self.x-self.y
obj1 = MyClass(10,20)
obj2 = MyClass(10,20)
obj3 = MyClass(20,20)
# print(str(obj1))
# print(repr(obj1))
# print(str(obj1) == str(obj2))
# print(repr(obj1) == repr(obj2))
# print(obj1 != obj1)
# print(eq(obj1,obj2))
# print(obj1 != obj3)
# print(obj1 != 42)
print(obj1 - obj3)
print(obj1 - 42)
#obj1+obj2
print(50-obj1)