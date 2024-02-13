# Day X: Lists

List are used to store multiple items is a single variable.

``` python
# scores.py

# Grades with variables
t1 = 100
t2 = 90
t3 = 70.5

# Grades with lists
grades = [100, 90, 80]
print(grades)
print(grades[0])
print(grades[1:2])

# Add grades to the list / Concatenate
grades = grades + [70, 60, 50]
print(grades)   
# [100, 90, 80, 70, 60, 50]

grades *= 2     # concatenates a copy of the current list to the end
print(grades)
# [100, 90, 80, 70, 60, 50, 100, 90, 80, 70, 60, 50]

# The 'append' method
grades = [100, 80, 70]
grades.append(42)
print(grades)
# [100, 80, 70, 42]

# List are mutable
grades[1] = 100
print(grades)
# [100, 100, 80, 42]

## Wrong ways...
grades = grades.append(42)  # deletes current grade list
grades + [42]               # does not save new item
grades = grades + 42        # list concatenation requires two lists


# Iterating over a list
for grade in grades:
    print(grades)
```

## Exercise

Write a program that counts the number of A's, B's, C's, and failures in a list of grades. Use a 10-point scale.

```python
# generates random list of 30 grades
from random import randrange

grades = []
for i in range(30):
    grades.append(randrange(100))
print(grades)

# create counter variables
a = 0
b = 0
c = 0
fail = 0

# start iterating through list
# check in which range each grade lies
# and add to appropriate counter
for grade in grades:
    if grade > 90:
        a += 1
    elif 80 < grade <= 90:
        b += 1
    elif 70 < grade <= 80:
        c += 1
    else:
        fail += 1

# output
print ("A's: ", a)
print ("B's: ", b)
print ("C's: ", c)
print ("Fails: ", fail)
```

## Modifying lists

```python
### Use indexing when modifying elements
## Taxes
prices = [0.99, 14.95, 7.00]

# Undesired behavior
for p in prices: # makes a 'copy' of each element and stores it in p
    p *= 1.07
   
# notice prices haven't changed
print(prices)   # [0.99, 14.95, 7.00]

# Correct: use indexing to modify original list (if absolutely necessary)
for index in range(len(prices)):
    prices[index] *= 1.07

print(prices)   # [1.0593000000000001, 15.996500000000001, 7.49]

### Searching
my_grocery_list = ['milk', 'cake', 'pizza']
if 'cake' in my_grocery:
    print('yum!')
else:
    print('nope')
    
```

## Removing elements

``` python
c = [1, 2, 3]

# Remove a specific item
my_list = c[:] # makes a copy of c called my_list
my_list.remove(1)
print(my_list)
print(c)

# Aliasing
# The association of a variable with an object is called a reference.
# In this example there are two references to the same object
alias_list = c # make an alias for c called alias_list
alias_list.remove(1)
print(c)

# Trying to remove an element that is not in the list raises an error
c.remove(4) # Error
if 4 in c:
    c.remove(4)
 
# Removing an item by index
del c[0]    # del is an operator
print(c)

# Remove and store the item in a variable using the pop method
value_at_zero = c.pop(0)
print(c)
print(value_at_zero)
```

See [PythonTutor Example of Aliasing](https://pythontutor.com/visualize.html#code=%23%20Initialize%20list%20c%0Ac%20%3D%20%5B1,%202,%203%5D%0A%0A%23%20Copy%20list%20c%0Amy_list%20%3D%20c%5B%3A%5D%0A%0A%23%20Remove%201%20from%20my_list%0Amy_list.remove%281%29%0A%0A%23%20Create%20an%20alias%20to%20list%20c%0Aalias_list%20%3D%20c%0A%0Aalias_list.remove%281%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).

## Various Methods

``` python
# sort method
my_list = [9, 3, 11]
my_list.sort()          # modifies original list
print(my_list)          # [3, 9, 11]


# sorted function
my_list = [9, 3, 11]
print(sorted(my_list))  # returns a copy that is sorted
print(my_list)          # [9, 3, 11]

my_list.reverse()       # modifies original list
print(my_list)          # [11, 3, 9]


# index
my_list = [9, 3, 11]
print(my_list.index(3)) # 1
print(my_list.index(5)) # ValueError


# extrema
print(min(my_list))     # 3
print(max(my_list))     # 9


# split
text = "Hello world!"
words = text.split()
print(words)            # ['Hello', 'World!']

scores = '90,67,87,102,77,80'
nums = scores.split(',')
print(nums)             # ['90', '67', '87', '102', '77', '80']


# list
letters = list("hello") 
print(letters)          # ['h', 'e', 'l', 'l', 'o']
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(10))         # # TypeError: 'int' object is not iterable


# join (string method)
"".join(letters)        # 'hello'
```

## Exercise

``` python
# Exercise: Grocery List Input
# Write a function make_grocery_list
# Adds grocery items to a list as they are input, until the user enters "done".
# Prints the sorted list

def make_grocery_list():
    # initialize empty list
    grocery_list = [] 
    item = ""

    # adds items to list
    while item != 'done':
        item = input('Enter a grocery item or "done": ')
        grocery_list.append(item) # add to list

    # delete "done"
    grocery_list.pop(-1)

    # organize list alphabetically
    grocery_list.sort() 

    print()
    
    for item in grocery_list:
        print(item)


make_grocery_list()
```

## Nested List

``` python
##### Nested Lists #####
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix = [[1, 2, 3],    # Cleaner code
          [4, 5, 6],
          [7, 8, 9]]

print(matrix[1][1])     # 5
```

## Tuples

``` python
##### Tuples #####

# Tuples are essentially immutable lists.
dimensions = (1920, 1080)
print(dimensions[0])
print(dimensions[1])
dimensions[0] = 1080 # TypeError

# reassign a tuple by overwriting it
dimensions = (1280, 720)
```

## Comprehensions

``` python
##### List Comprehensions #####

my_squares = []
for x in range(10):
    my_squares.append(x**2)
    
print(my_squares)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Syntax: [var_expression for var in iterable if condition]
# if condition is optional

# {x^2 : x in [0, 9)}
my_squares = [x**2 for x in range(10)]
print(my_squares)   # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Exercise: Generate a list of the first four positive powers of 2.
my_powers = [2**n for n in range(1, 5)]
print(my_powers)    # [2, 4, 8, 16]


# Find all of the number from 1-100 that are divisible by 7
div_by_7 = [x for x in range(101) if x % 7 == 0]
print(div_by_7)    # [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]


# Exercise: Find all of the words in a string that are less than 4 letters.
s = 'the quick brown fox jumped over the lazy dog'
small_words = [word for word in s.split() if len(word) < 4]
print(small_words)  # ['the', 'fox', 'the', 'dog']


# Exercise: Find the sum of all digits of an inputted number
number = "123"
s = sum([int(d) for d in number])
print(s)    # 6

# Tuple comprehensions use parentheses () instead of brackets [].
```

## List Comprehension Exercises

Find all of the numbers from 1-1000 that have a 3 in them.

Count the number of spaces in a string.

Remove all of the vowels in a string.

## Comprehension Challenges

Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)

For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit by which a number is divisible.

# TODO: Command Line Arguments

# Day 16: Dictionaries

## Dictionaries

[https://docs.python.org/3.8/tutorial/datastructures.html#dictionaries](https://docs.python.org/3.8/tutorial/datastructures.html#dictionaries)

### Dictionary Syntax

``` python
##### Dictionaries #####
# A dictionary is more general than a list.
# A list's elements were accessed using integer indices.
# A dictionary's elements are accessed by using key.

# Initialize an empty dictionary
eng2sp = dict()     # This one has some other advantages (see documentation)
eng2sp = {}
print(eng2sp)

# Add elements to a dictionary
eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp['two'] = 'dos'
print(eng2sp)

# New in Python 3.6 Dictionaries are ordered in the way you add items.
eng2sp['three'] = 'tres'

# Create/Update a dictionary
# Syntax: {key: value, ...}
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# eng2sp = {            Alternative declaration for readability
#     'one': 'uno',
#     'two': 'dos',
#     'three': 'tres'
# }

print(eng2sp)

# Access elements in a dictionary
print(eng2sp['two'])
print(eng2sp['four']) # KeyError
```

### Dictionary Comprehension

Use a dictionary comprehension to count the length of each word in a sentence.

### Iterating through Dictionaries

``` python
### Iterate through a dictionary
# Looks at keys by default
for entry in eng2sp:
    print(entry) 

for key in eng2sp.keys():
    print(key)

print('one' in eng2sp)  # True
print('uno' in eng2sp)  # False

# Iterate through values
for value in eng2sp.values():
    print(value)

# Iterate through key and values
for key, val in eng2sp.items():
    print(key, val)
```

### Dictionaries as a Collection of Counter

``` python
### Dictionaries as a collection of counters
# Suppose you are given a string and want to count how many times each letter appears.
def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            # create the key is not present
            d[c] = 1
        else:
            # increment the value if k is present
            d[c] += 1
    return d

def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

h = histogram('parrot')
print(h)    # {"p": 1, "a": 1, "r": 2, "o": 1, "t": 1}
```

## Passing by reference

[Python Tutor - Passing by Reference](https://pythontutor.com/visualize.html#code=a%20%3D%20%5B1,%202,%203%5D%0A%0Adef%20f%28lst%29%3A%0A%20%20%20%20lst.append%284%29%0A%0Af%28a%29%0A%0Aprint%28a%29&cumulative=false&curInstr=7&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Memoization

``` python
# Fibonacci Revisited
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

[Fibonacci Memoization Tree](https://youtu.be/oBt53YbR9Kk?t=1913)

# Day 17: Memoization

## Memoization

``` python
# Fibonacci Revisited
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

[Fibonacci Memoization Tree](https://youtu.be/oBt53YbR9Kk?t=1913)

## Alternative

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