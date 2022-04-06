from operators import MyClass

obj1 = MyClass(10, 20)
obj2 = MyClass(10, 20)
obj3 = MyClass(20, 20)
WIDTH = 80


def example_operator():
    header("Operator")
    x = 10
    y = 20
    z = x + y
    print("Value of z is: ", end="")
    print(z)
    print("Type of z is: ", end="")
    print(type(z))
    a = "Hello "
    b = "World"
    c = a + b
    print("Value of c is: ", end="")
    print(c)
    print("Type of c is: ", end="")
    print(type(c))
    footer()


def example_not_overloaded_addition():
    header("Not overloaded operator")
    obj1 = MyClass(10, 20)
    obj2 = MyClass(10, 20)
    try:
        # Since this will raise an exception,
        # catch it here to keep the program running
        obj1 + obj2
    except TypeError:
        print("This is not gonna work")
    footer()


def example_str_and_repr():
    header("__str__ and __repr__")
    print("Calling __str__ of obj1: ", end="")
    print(str(obj1))
    print("Calling __repr__ of obj1: ", end="")
    print(repr(obj1))
    print(str(obj1) == str(obj2))
    print(repr(obj1) == repr(obj2))
    footer()


def example_eq():
    header("__eq__")
    print(obj1 != obj2)
    print(obj1 != obj3)
    print(obj1 == 42)
    footer()


def example_rsub():
    header("__rsub__")
    print(obj1 - 42)
    print(50 - obj1)
    print(obj1 - obj3)
    footer()


def header(title):
    length = (WIDTH - len(title))//2
    s = '=' * length + title + '=' * length
    print("")
    print(s)


def footer():
    print('=' * WIDTH)


if __name__ == "__main__":
    example_operator()
    example_not_overloaded_addition()
    example_str_and_repr()
    example_eq()
    example_rsub()
