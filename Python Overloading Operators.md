# Python Overloading Operators
Today we want to talk about overloading operators in python. After today's lecture you will know what is overloading operators and be able to overload some operators like what we did in the Haskell part in ex4 to instance a data to class Show and Eq etc.
### What is operators?
Operators in python are +, -, etc. Generally, operators are some actions you can do on an object which are invoked by special syntax (such as arithmetic operations or subscripting and slicing)(Referenced [here][1]).

Using these operators we can implements addtion, subtraction and printing the object quickly and easily. Of course, we have many built-in operators and for each different built-in class (like str, int) the built-in operators have different effects.

**An example for class int**
```
x = 10 # x is an int
y = 20 # y is an int
z = x + y # the default behaviour of built-in operator "+" for class int is addtion
print(z) # built-in operator print with an int variable as input
# this will output 30
```
**An example for class str**
```
a = "Hello " # a is a str
b = "World" # b is a str
c = a + b # the default behaviour of built-in operator "+" for class str is concatenation
print(c) # built-in operator print with an str variable as input
# this will output Hello World
```
### What is overloading
In the perspective of an object oriented programming language, two or more methods with the same name but different types of arguments in a single class is called overloading.

However Python does not allow two methods with same name. To achieve that goal, you can create a method with header: foo(a=None). Both foo() and foo("test") will work. We won't discuss this further since it is out of topic.

What Python actually allows is operator overloading. Since we have introduced operators above and operators have different effects for different classes, now you may have a new question: Can I use these operators for user defined classes? The answer is that you can use some operators for your defined class like `==` because they have default implementations, but many other operators need to be overloaded by yourself. Also, all built-in operators can be overloaded, but we can not create new operator.

**An example for calling an operator without default implementation**
```
class MyClass:
    def __init__(self,x=0,y=0): # this is constructor for class MyClass,x=0 means
        self.x = x              # if we didn't give x when we creating an object, 
        self.y = y              # the default value for x is 0. Same logic to y

obj1 = MyClass(10,20)
obj2 = MyClass(10,20)
obj1 + obj2
```
output
```
Traceback (most recent call last):
  File "operators.py", line 14, in <module>
    print(p1+p2)
TypeError: unsupported operand type(s) for +: 'Myclass' and 'Myclass'
```
The above error means python doesn't know what to do with operator + in class MyClass, since we didn't provide implementation for operator + for MyClass
### How to overload operators
Similar to what we did in lecture and ex4, we just need to write a function for each operator you want to overload in your class. Since there are many [different operators](https://docs.python.org/3/reference/datamodel.html#special-method-names) and we can't cover all of them in this lecture, we will focus on some important operators. 
Before we start talking about specific operators, there are some general knowledge you need to know. A function starts and ends with double underscore __ is a special function. Unlike other generic function, this kind of functions can determine the behaviour of an operator or a native function for its class, sometimes it is a hook that python calls under specific situations. For instance, in the above example, `__inti__` will be called when the object is created.
#### `__str__` and `__repr__`
These operators are similar to an instance of class Show in haskell, we will discuss the difference between them.
`__repr__`: When you defined a new class, your class has `__repr__` method by default and it will return a string that represents the address of the object by default.
`__str__`: Once this function has been overloaded, you can use `print()`, `str()` or `format()` to output the object in string, if you haven't overloaded this function, we will call `__repr__` to replace this function.
Now you may want to ask why we need to overload both function instead of only overloading `__repr__`? The reason is `__repr__` should be used to represent an unambiguous result and `__str__` should be represent a readable result. In other words, `__repr__` is for developers and `__str__` is for users.
**An example of difference between `__str__` and `__repr__`**
Before overloading `__str__`
```
print(obj1) # we haven't overloaded __str__, now it calls
print(obj2) #  __repr__
```
output
```
<__main__.MyClass object at 0x10cdd6c40>
<__main__.MyClass object at 0x103fbfdf0>
```
After overloading `__str__`
```
class MyClass:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __repr__(self):  # you don't need to overload __repr__ to get __str__, we will use it later so overload it right now
        return "Call from repr " + "<%s object at %r>" % (self.__class__.__name__, hex(id(self)))

obj1 = MyClass(10, 20)
obj2 = MyClass(10, 20)
print(obj1)
print(obj2)
```
outout 
```
(10,20)
(10,20)
```
Now you can see if we have 2 different objects with same value, `__repr__` will give us an unambiguous result but `__str__` has the same output. Therefore, using `__repr__` helps developers to debug quickly(like using `eval()` to compare two objects) and using `__str__` helps users to know what do we have inside the objects, so they have different usage and you should choose an appropriate way between these two methods.

You can call different methods for different usage:
```
print(repr(obj1)) # this is same as print(obj1.__repr__())
print(str(obj1)) # this is same as print(obj1)
print(str(obj1) == str(obj2)) #str of obj1 and obj2 are same
print(repr(obj1) == repr(obj2)) #repr of obj1 and obj2 are not same
```
output
```
(10,20)
Call from repr <MyClass object at 0x103fa4fd0>
True
False 
```
#### `__eq__`
By defualt, `__eq__` will compare whether two objects are same, in other words, it will check the address of two objects. After overloading this method we can compare two objects by their value inside. Also, we can check whether two objects are both MyClass at first. This is similar to writing an instance of class Eq in haskell. To save space, I will only show the method `__eq__` below, which should be placed below `def __repr__` in the example above
```
def __eq__(self,other): # if we don't overload this operator, it will compare two objects' address
    if isinstance(other, MyClass):
        return self.x == other.x and self.y == other.y
    return False
```
**Excuting `__eq__`**
```
obj3 = MyClass(20,20)
print(obj1 == obj2)
print(obj1 == obj3)
print(obj1 == 42)
```
**Output**
```
True
False
False
```
Like Haskell, once you overload ==, you don't need to overload != again, python will do this for you
```
print(obj1 != obj2)
print(obj1 != obj3)
```
Output
```
False
True
```
#### `__sub__` and `__rsub__`
Unlike `__eq__`, we don't have default implementation for `__sub__`, this means we have to overload this operator otherwise we can't use operator '-' between two MyClass objects. Notice that argument 'other' in this method is the variable after operator '-'.
```
def __sub__(self,other):
    if isinstance(other, MyClass):
        return MyClass(self.x - other.x, self.y - other.y)
    return "Not MyClass objects"
```
**Excuting `__sub__`**
```
print(obj1 - obj3)
print(obj1 - 42)
```
**Output**
```
(-10,0)
Not MyClass objects
```
`__rsub__` is a very interesting implementation, after implmenting this function, you can subtract 2 objects with different classes. Again, we don't have default implementation for this one. Remember, in `x-y`, if x and y are not in the same class, you have to implement `__rsub__` for y's class and put y **after** `-` to call `__rsub__`; If x and y are in the same class, we will call `__sub__`. If `__sub__` is not defined, it won't call `__rsub__` for the same class objects but gives you an error. 
```
def __rsub__(self,other):
    return other-self.x-self.y
```
**Excuting`__rsub__`**
```
print(obj1-42)
print(50-obj1)
print(obj1 - obj3)
```
**Output**
```
Not MyClass objects
20
(-10,0)
```
### How overloading operator works
Now we have learned what is operator overloading, but how exactly did Python achieved the mechanism where implementing a function changes the behaviour of "x + y"?
In Python, when calling an operator, the corresponding method (that we implement to overload) is automatically invoked. For an example of an unary operation `str()` and its corresponding method `__str__(self)` defined in class MyClass, given an instance x, calling
```
str(x)
```
is equivalent to
```
type(x).__str__(x)
```
Similarly for the binary operation `+` and the corresponding method `__add__(self, other)` defined in class MyClass, given an instance x, calling
```
x + y
```
is equivalent to
```
type(x).__add__(x, y)
```
regardless of the class of y
### Conclusion
We can write different methods for own defined class to implement `==`,`+` and many other operators. Some operators have their default methods like `==` but more operators need to be overloaded by you!

[1]: https://docs.python.org/3/reference/datamodel.html