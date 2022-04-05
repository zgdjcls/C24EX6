from operators import MyClass

def example_operator():
    x = 10
    y = 20
    z = 10+20
    print(type(z))
    a = "Hello "
    b = "World"
    print(type(a+b))

def example_not_overloaded_addition():
    obj1 = MyClass(10, 20)
    obj2 = MyClass(10, 20)
    try:
        obj1 + obj2
    except  TypeError:
        print("This is not gonna work")
        
# obj3 = MyClass(20, 20)
# print(str(obj1))
# print(repr(obj1))
# print(str(obj1) == str(obj2))
# print(repr(obj1) == repr(obj2))
# print(obj1 != obj1)
# print(eq(obj1,obj2))
# print(obj1 != obj3)
# print(obj1 != 42)
# print(obj1 - obj3)
# print(obj1 - 42)
# # obj1+obj2
# print(50-obj1)
