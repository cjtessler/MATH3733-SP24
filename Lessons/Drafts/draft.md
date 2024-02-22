# Day X: Memoization and Passing by Assignment

## Memoization

Let's revisit the Fibonacci sequence.

[Fibonacci Visualization 6:25 - 11:00](https://youtu.be/oBt53YbR9Kk?start=384)

Discuss how many leaves there are at level *n*.

``` python
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

memo = {
    1: 1, 
    2: 1
}

def fib_memo(n: int, memo: dict) -> int:
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]


from time import time
n = 35

start = time()
print(fib(n))
end = time()
print(f"fib({n}) took {end-start} seconds")         # 3.393 seconds

start = time()
print(memo_fib(n, memo))
end = time()
print(f"memo_fib({n}) took {end-start} seconds")    # 0.000038 seconds
```

[Fibonacci Memoized Tree](https://youtu.be/oBt53YbR9Kk?t=1913)

The following definition of `fib_memo` does not require the declaration of a `memo` with the base cases pre-initialized.

``` python
def fib_memo(n: int, memo: dict = {}) -> int:
    if n in memo:
        return memo[n]
    elif n <= 2:
        return 1
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]
```

## Passing by Assignment

Values can be passed to function either "by value" or "by reference" depending on the data type. Immutable data types are passed by value, whereas mutable data types are passed by value. Here is a summary of various data types in Python:

| Data Type    | Built-in Class      | Mutable |
|--------------|---------------------|---------|
| Numbers      | int, float, complex | ❌       |
| Strings      | str                 | ❌       |
| Tuples       | tuple               | ❌       |
| Bytes        | bytes               | ❌       |
| Booleans     | bool                | ❌       |
| Frozen sets  | frozenset           | ❌       |
| Lists        | list                | ✅       |
| Dictionaries | dict                | ✅       |
| Sets         | set                 | ✅       |
| Byte arrays  | bytearray           | ✅       |

Let's look at an example to understand the difference between passing by value and passing by reference.

```python
def func(x: int, y: list) -> None:
    x = x + 1
    y.pop()

if __name__ == "__main__":
    i = 1
    lst = ['a', 'b']

    func(i, lst)

    print(i, lst)   # 1 ['a']
```

If you pass an copy of the list using the `copy` method of `[:]` syntax, then the list will not change.

```python
def func(x: int, y: list) -> None:
    x = x + 1
    y.pop()

if __name__ == "__main__":
    i = 1
    lst = ['a', 'b']

    func(i, lst[:])

    print(i, lst)   # 1 ['a', 'b']
```

## Operator: `is`

The `is` keyword is used to check if variables are referencing the same object. It 

```text
>>> l = ['a', 'b', 'c']
>>> m = l
>>> n = l.copy()
>>> m == l
True
>>> n == l
True
>>> l
['a', 'b', 'c']
>>> m
['a', 'b', 'c']
>>> n
['a', 'b', 'c']
>>> l is m
True
>>> m is l
True
>>> n is l
False
>>> l.pop()
'c'
>>> l
['a', 'b']
>>> m
['a', 'b']
>>> n
['a', 'b', 'c']
>>> id(l)
4303458176
>>> id(m)
4303458176
>>> id(n)
4303478912
```

Recommended Reading: [Python's Mutable vs Immutable Types: What's the Difference?](https://realpython.com/python-mutable-vs-immutable-types/) on Real Python


# Day 21: LaTeX

[https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)

# Day 22: Object-oriented Programming

Object-Oriented Programming

We write classes to represent real-world objects and situations, and we create objects based on these classes.

When we write a class, we define the general behavior that a whole category of objects can have.

## Classes

```python
### Example: Turtle ###
# import the Turtle class from the turtle module
from turtle import Turtle

# instantiate a turtle object from the class
Bob = Turtle()
Bob.color('blue')
Bob.shape("turtle")
Bob.forward(100)

# instantiate a second turtle object from the class
Katie = Turtle()
Katie.color('red')
Katie.left(180)
```

## dog.py

```python
### Creating and Using a Class
# dog.py
class Dog():    # convention: names of classes are capitalized
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):  # runs whenever an object is instantiated
        """Initialize name and age attributes."""
        # Any variable prefixed with self is available to every method in the class
        self.name = name
        self.age = age
        
    def sit(self):  # a method is a function that is a part of a class
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over.")
        
 ### Making an instance from a class
my_dog = Dog('willie', 6)

# we use dot notation to access class attributes and methods
print("My dog's name is " + my_dog.name + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
```

## restaurant.py v1

```python
# Exercise: restaurant.py
'''
Make a class called  Restaurant. The  __init__() method for Restaurant should store two attributes: a restaurant_name and a food_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
'''

class Restaurant():
    """A simple attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, food_type):
        """Initialize attributes."""
        self.restaurant_name = restaurant_name
        self.food_type = food_type
        
    def describe_restaurant(self):
        """Prints a description of the restaurant."""
        print(f"{self.restaurant_name.title()} serves {self.restaurant_type}.")
        
    def open_restaurant(self):
        """Opens the restaurant."""
        print(f"{self.restaurant_name.title()} is open!")
        

pizza_place = Restaurant("Palace Pizza", "pizza")

print(pizza_place.restaurant_name)
print(pizza_place.restaurant_type)
pizza_place.describe_restaurant()
pizza_place.open_restaurant()
```

## car.py

``` python
### Working with Classes and Instances

class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        
    def __str__(self):
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{str(self.year)} {self.make} {self.model}"
        return long_name.title()


my_old_car = Car('chevy', 'lumina', 1994)   # Create instance of the car
print(my_old_car)
print(my_old_car.get_descriptive_name())    # Calls method

# Add __str__ method then print
print(my_old_car)
```

## car.py v2

Add odometer_reading.

``` python
### Setting a Default Value for an Attribute

class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # Added
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def get_odometer(self):
        return self.odometer_reading
    
    def read_odometer(self): # added
        """Print a statement showing the car mileage."""
        print(f"This car has {self.odometer_reading} miles on it")


my_old_car = Car('chevy', 'lumina', 1994)

# odometer
my_old_car.read_odometer()
my_old_car.odometer_reading = 100000
my_old_car.read_odometer()
```

``` python
class Car():
    """A simple attempt to represent a car."""
    # -- snip-- #
    
    def set_odometer(self, mileage):
        """
        Set the odometer reading to a given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

        
my_old_car = Car('chevy', 'lumina', 1994)

my_old_Car.set_odometer(10000)   # Better practice
my_old_car.read_odometer()

my_old_car.increment_odometer(10)
my_old_car.read_odometer()

my_old_car.update_odometer(0)
```

# Day X: Algorithmic Complexity