# Day 5

## Plan

- Functions
- 

## Basic Functions

```python
def my_func():
    print("My first function")

my_func()
print(my_func()) # prints None because first_function does 'return' information
```

We will now learn to define our own functions.

### Returning Functions

We can use a docstring to explain what the function does. Talk about code intelligence

```python
# This defines the function
def absolute_value(x):  # x is a formal parameter
    '''Returns the absolute value of the input.'''
    if x < 0:
        return -x
    else:
        return x

absolute_value(-10) # calls the function, but doesn't print its return value
print(absolute_value(-10))
a = absolute_value(-10)
print("The absolute value of -10 is", a)
```

The `x` in the parentheses in the function’s definition is a **formal parameter**.

When the function is called with an argument (-10, above), the argument is assigned to the formal parameter in the function.

As soon as a `return` statement is encountered, the value of the expression following the `return` statement is returned to the caller and no other code is executed in the function.

## Modules

A module is a file that contains a collection of related functions.

``` python
>>> import math
>>> math
<module 'math' (built-in)>
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> sin(0)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    sin(0)
NameError: name 'sin' is not defined
>>> math.sin(0)
0.0
>>> math.pi
3.141592653589793
>>> math.sin(math.pi)
1.2246467991473532e-16              # VERY small float
>>> from math import sin, pi        # Removes need for dot notation
>>> pi
3.141592653589793
>>> sin(pi)
1.2246467991473532e-16
>>> 
```

[https://docs.python.org/3/library/math.html](https://docs.python.org/3/library/math.html)

## Exercise 1

Write a function that returns the area of a circle with a given radius.

``` python
import math

def area_of_circle(radius):
    a = math.pi * radius**2
    return a

# The following definition of the function is viable,
# but the use of a "temporary variable" can make debugging easier.
def area_of_circle(radius):
    return math.pi * radius ** 2

print(area_of_circle(4))
```

## Exercise 2

The function `math.sin(x)` returns the sine of `x` radians. Review code intellisense docstring.

Write a function `sin_of_degress(x)` that returns the sine of `x` degrees.

Recall pi radians == 180 degrees.

``` python
from math import sin, pi

def sin_of_degrees(x):
    rad = x * pi / 180 
    result = sin(rad)
    return result

print(sin_of_degrees(180))
```

# Day 08: Turtle

## Introduction to Turtle Module

[https://www.reddit.com/r/Python/comments/7mo2l8/turtle_module_drawing_a_randomised_landscape/](https://www.reddit.com/r/Python/comments/7mo2l8/turtle_module_drawing_a_randomised_landscape/)

[https://docs.python.org/3/library/turtle.html](https://docs.python.org/3/library/turtle.html)

**replit.com uses Python 2.7 for Turtle**

```python
import turtle

# We create a Turtle object and assign it to a variable named bob
bob = turtle.Turtle()
print(bob)
turtle.mainloop()
bob.shape("turtle")

# objects have methods, which is just a function attached to an object
bob.forward(100)
bob.left(90)
bob.forward(100)
```

### Exercise 1

Modify the program to draw a square.

```python
import turtle

# We create a Turtle object and assign it to a variable named bob
bob = turtle.Turtle()
turtle.mainloop()

# objects have methods, which is just a function attached to an object
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
```

We can do the same thing more concisely with a `for`  loop.

```python
for i in range(4):
    bob.forward(100)
    bob.left(90)
```

Write a function called square that takes a parameter named `t`, which is a turtle.

```python
# Wrapping a piece of code up in a function is called encapsulation.
# Attaches name to code, which serves as a kind of documentation.
# Allows easy code reuse
# If you ever find yourself copying and pasting, encapsulate the code
def square(t):
    '''Draws a square with sides of a given length
    The Turtle ends at the starting location.
    '''
    for i in range(4):
        t.forward(100)
        t.left(90)

square(bob)
```

### Exercise 2

Add another parameter, named `length`, to `square()`.

Modify the body so the length of the sides is `length`, and then modify the function call to provide a second argument.

Run the program again. Test your program with a range of values for length.

```python
# Adding a parameter to a function is called generalization
def square(t, length):
    '''Draws a square with sides of a given length
    The Turtle ends at the starting location.
    '''
    for i in range(4):
        t.forward(length)
        t.left(90)

square(bob, 10)
square(bob, 100)
square(bob, 1000)
```

### Exercise 3

Make a copy of `square` and change the name to `polygon`.

Add another parameter named `n` and modify the body so it draws an n-sided regular polygon.

Recall the exterior angles of an n-sided polygon are 360/n degrees.

```python
DEGREES_IN_CIRCLE = 360.0   # The explicit float is necessary in Python 2

def polygon(t, n=4, length=10):
    '''Draws a polygon with n sides.
    By default, it draws a square with side length 10.
    t: Turtle object
    n: number of line segments
    length: length (in pixels) of each side
    '''
    angle = 360.0 / n
    for i in range(n):
        t.forward(length)
        t.left(angle)

polygon(bob, n=11, length=100) # n and length are 'keyword arguments'
```

### Exercise 4

Write a function called `circle` that takes a turtle `t`, and radius `r` , as parameters and draws an approximate circle by calling `polygon` with an appropriate length and number of sides.

Test your function with a range of values for `r` .

``` python
import turtle
from math import pi

bob = turtle.Turtle()
turtle.mainloop()

# --snip--
    
def circle(t, r):
    '''Draws an approximated circle.'''
    circumference = 2 * pi * r
    n = 50
    length_per_side = circumference / n
    polygon(t, length_per_side, n)
    
    
circle(bob, 10)
circle(bob, 100)
circle(bob, 1000)
```

One limitation of this solution is that `n` is constant. Large values of `n` yield poor approximations. We do not want to complicate the **interface** by adding more parameters.

Choose an appropriate value of `n` depending on the circumference.

``` python
DEGREES_IN_CIRCLE = 360.0   # The explicit float is necessary in Python 2
                            # Division (/) does not automatically cast to float

def circle(t, r):
    ''' Draws an approximated circle.'''
    circumference = 2 * pi * r
    # n = (circumference / 3) + 3 to illustrate preconditions
    n = int(circumference / 3) + 3  # adding three guarentees the polygon has at least 3 sides
    length_per_side = circumference / n
    polygon(t, length_per_side, n)
```

# Day 09: More on Turtle, Scope

One limitation of this solution is that `n` is constant. Large values of `n` yield poor approximations. We do not want to complicate the **interface** by adding more parameters.

Choose an appropriate value of `n` depending on the circumference.

``` python
def circle(t, r):
    ''' Draws an approximated circle.'''
    circumference = 2 * pi * r
    # n = (circumference / 3) + 3 to illustrate preconditions
    n = int(circumference / 3) + 3  # adding three guarentees the polygon has at least 3 sides
    length_per_side = circumference / n
    polygon(t, length_per_side, n)
```

## Exercise 5

Make a more general version of `circle` called `arc` that takes an additional parameter, `angle`, which determines what fraction of the circle to draw.

`angle` is in units of degrees, so when `angle=360`, `arc` should draw a complete circle.

```python
def arc(t, r, angle):
    arc_length = 2 * pi * r * (angle / 360)
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    
    for i in range(n):
        t.forward(step_length)
        t.left(step_angle)
```

We have used the same code in multiple places.

```python
# Refactoring
def polyline(t, n, length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

    
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
    
    
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
 

def circle(t, r):
    arc(t, r, 360)
```

## Functions

Functions are reusable pieces of code.

Functions are not run in a program until they are "called" or "invoked" in a program.

Function characteristics:

- has a **name**
- has **parameters** (0 or more)
- has a **docstring** (optional but recommended)
- has a **body**
- **returns** something (`None` is nothing specified)

Called a function creates a new **scope/frame/environment**.

[Python Tutor - Scope Example 1](https://pythontutor.com/visualize.html#code=def%20f%28x%29%3A%20%23%20name%20x%20used%20as%20formal%20parameter%20%0A%20%20%20%20y%20%3D%201%20%0A%20%20%20%20x%20%3D%20x%20%2B%20y%20%0A%20%20%20%20print%28'x%20%3D',%20x%29%20%0A%20%20%20%20return%20x%20%0A%20%20%20%20%0Ax%20%3D%203%20%0Ay%20%3D%202%20%0Az%20%3D%20f%28x%29%20%23%20value%20of%20x%20used%20as%20actual%20parameter%20%0Aprint%28'z%20%3D',%20z%29%20%0Aprint%28'x%20%3D',%20x%29%20%0Aprint%28'y%20%3D',%20y%29%20&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

``` python
def f(x): # name x used as formal parameter 
    y = 1 
    x = x + y 
    print('x =', x) 
    return x 
    
x = 3 
y = 2 
z = f(x) # value of x used as actual parameter 
print('z =', z) 
print('x =', x) 
print('y =', y) 
```

[Python Tutor - Scope Example 2](https://pythontutor.com/visualize.html#code=def%20f%28x%29%3A%20%0A%20%20%20%20def%20g%28%29%3A%20%0A%20%20%20%20%20%20%20%20x%20%3D%20'abc'%20%0A%20%20%20%20%20%20%20%20print%28'x%20%3D',%20x%29%20%0A%0A%20%20%20%20def%20h%28%29%3A%20%0A%20%20%20%20%20%20%20%20z%20%3D%20x%20%0A%20%20%20%20%20%20%20%20print%28'z%20%3D',%20z%29%20%0A%0A%20%20%20%20x%20%3D%20x%20%2B%201%20%0A%20%20%20%20print%28'x%20%3D',%20x%29%20%0A%20%20%20%20h%28%29%20%0A%20%20%20%20g%28%29%20%0A%20%20%20%20print%28'x%20%3D',%20x%29%20%0A%20%20%20%20return%20g%20%0A%0Ax%20%3D%203%20%0Az%20%3D%20f%28x%29%20%0Aprint%28'x%20%3D',%20x%29%20%0Aprint%28'z%20%3D',%20z%29%20%0Az%28%29%20&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

``` python
def f(x): 
    def g(): 
        x = 'abc' 
        print('x =', x) 

    def h(): 
        z = x 
        print('z =', z) 

    x = x + 1 
    print('x =', x) 
    h() 
    g() 
    print('x =', x) 
    return g 

x = 3 
z = f(x) 
print('x =', x) 
print('z =', z) 
z() 
```