
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