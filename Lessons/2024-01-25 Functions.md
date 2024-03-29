# Day 5: Functions

## Announcement

- Project 1 Due at 11:59 PM. For submission:
    1. Create a folder titled `LastName_P1`, where LastName is your last name (e.g., `Tessler_P1`).
    2. Put your implementations `change.py`, `savings.py`, and `change_challenge.py` in the folder.
    3. Right-click on the folder and download the folder.
        - You might need to create an empty folder on your local system to save the folder.
    4. Compress the folder by right-clicking on the folder.
    5. Upload the folder to MyFire.
- Project 2 will be posted by the end of the weekend. Be sure to work regularly.
- Code daily!

## Plan

- Bisection Method
- Functions

## Bisection Method

Here is an implementation of the bisection search.

```python
# Find the square root of a number x
x = int(input(">"))
epsilon = 0.01
low = 0
high = max(1, x)
guess = (high + low) / 2
num_guesses = 1

# Perform bisection search for the square root
while abs(guess ** 2 - x) >= epsilon:
    print(f"low: {low}, high: {high}, guess: {guess}")
    num_guesses += 1
    if guess ** 2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2

# Outside the while loop
print("Number of guess:", num_guesses)
print(guess, "is close to the square root of x")
```

## Exercise

Empire State Building is 102 stories high. A man wants to know the highest floor from which he could drop an egg without the egg breaking. He proposed to drop an egg from the top floor, and if it broke, he would go down one floor and try again. At worst, this method would take 102 eggs. In the worst-case scenario (the egg always breaks), how many eggs would be used if he used a bisection search instead?

**Solution:** He would test on the following floors:

- `102`
- `(0 + 102) // 2 = 51`
- `(0 + 51) // 2 = 25`
- `(0 + 25) // 2 = 12`
- `(0 + 12) // 2 = 6`
- `(0 + 6) // 2 = 3`
- `(0 + 3) // 2 = 1`

He would use 7 eggs. Notice $\log_2(102) \approx 7$.

## Functions

We will now learn to define our own functions. Functions are reusable pieces of code.

```python
def my_func():
    print("My first function")

my_func()
print(my_func()) # prints None because first_function does 'return' information
```

Functions are not run in a program until they are "called" or "invoked" in a program. A function is called with parentheses.

Function characteristics:

- **name**: The name of a function follows the `def` keyword.
- **parameter(s)**: The parameters are in the parentheses following the function's name. There are zero or more parameters.
- **argument(s)**: The arguments are the values passed to the function's parameters when the function is called.
- **body**: The body of a function is indented (typically four spaces) and defines the logic of the function.
- **docstring**: A docstring is in triple quotes on the first line of the body, and it explains the usage of the function
- **`return`**: A `return` statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller.

```python
# This defines the function
def absolute_value(x):  # x is a parameter
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

The `x` in the parentheses in the function’s definition is a **parameter**.

When the function is called with an **argument** (-10, above), the argument is assigned to the parameter in the function.

As soon as a `return` statement is encountered, the value of the expression following the `return` statement is returned to the caller and no other code is executed in the function.

### Modules

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

Write a function `sin_of_degrees(x)` that returns the sine of `x` degrees.

Recall pi radians == 180 degrees.

``` python
from math import sin, pi

def sin_of_degrees(x):
    rad = x * pi / 180 
    result = sin(rad)
    return result

print(sin_of_degrees(180))
```

## Exercises

Complete exercises 16 through 19.
