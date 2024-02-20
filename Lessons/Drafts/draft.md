

# Day 16: Dictionaries

## Dictionaries

[https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

### Dictionary Syntax

``` python
# A dictionary is more general than a list.
# A list's elements were accessed using integer indices.
# A dictionary's 'values' are accessed by using 'keys'.
# It's elements are key-value pairs.

# Initialize an empty dictionary
eng2sp = dict()
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

### Dictionary Comprehension

Use a dictionary comprehension to count the length of each word in a sentence.

```python
sentence = "The quick brown fox jumps over the lazy dog"
word_lengths = {}  # Initialize an empty dictionary

# Split the sentence into words and loop through each word
for word in sentence.split():
    word_lengths[word] = len(word)  # Set the word as key and its length as value in the dictionary

word_lengths = {word: len(word) for word in sentence.split()}
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

### Exercise

Create a Contacts Dictionary:

1. Start by creating an empty dictionary named `contacts`.
    - Add three contacts to the dictionary. Each contact should have a name as the key and their phone number as the value.

2. Add a New Contact:
    - Prompt the user to enter a new contact name and their phone number.
    - Check if the contact already exists in the dictionary. If it does, print a message saying the contact is already in the dictionary. Otherwise, add the new contact to the dictionary.
  
3. Update a Contact's Phone Number:

    - Prompt the user to enter the name of a contact whose phone number they want to update.
    - If the contact exists, prompt for the new phone number and update the contact's phone number in the dictionary. If the contact does not exist, print a message saying so.

4. Retrieve and Display a Contact's Phone Number:

    - Prompt the user to enter the name of a contact whose phone number they wish to retrieve.
    - Check if the contact exists in the dictionary. If it does, print the contact's name and phone number. If not, print a message indicating that the contact was not found.

5. Bonus: Display All Contacts:

    - Write a piece of code that prints all the contacts in the dictionary, formatted nicely. For example, each contact should be printed on a new line with the format: `Name: Phone Number`.

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