# Day X: Object-oriented Programming

We write classes to represent real-world objects and situations, and we create objects based on these classes.

When we write a class, we define the general behavior that a whole category of objects can have.

Making an object from a class is called **instantiation**, and you work with **instances** of a class.

## Turtle

```python
### Example: Turtle ###
# Import the Turtle class from the turtle module
from turtle import Turtle

# instantiate a turtle object from the class
Bob = Turtle()      # Bob is an 'instance' of Turtle
Bob.color('blue')
Bob.shape("turtle")
Bob.forward(100)

# instantiate a second turtle object from the class
Katie = Turtle()    # Katie is another 'instance' of Turtle
Katie.color('red')
Katie.left(180)
Katie.forward(100)
```

## Dog

Let's learn how to create and use classes of our own. Create a file named `dog.py`. Files containing classes definitions are called **modules** (more on this later).

```python
# dog.py
class Dog:    # convention: names of classes are capitalized
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):  # runs whenever an object is instantiated
        """Initialize name and age attributes."""
        # Any variable prefixed with self is available to every method in the class
        # These are called 'attributes'
        self.name = name
        self.age = age
        
    # def sit(self):  # a 'method' is a function that is a part of a class
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
           print(f"{self.name} rolled over!")

# Making an instance from a class
my_dog = Dog('Willie', 6)

# we use dot notation to access class attributes and methods
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```

### Exercise

1. Add a third attribute called `breed` so that the user can specify the breed of the dog. Then use the attribute in a printed sentence.

2. Modify the class so that the dog's name is always uppercase, regardless of how the user instantiated the `Dog`.

```python
class Dog:

    def __init__(self, name, age, breed):
        """Initialize name and age attributes."""
        self.name = name.title()
        self.age = age
        self.breed = breed

    # --snip--

riley = Dog("riley", 11, "German Shepherd")
print(f"My dog, {riley.name}, was an {riley.age}-year old {riley.breed}!")
```

## Car

Create a `Car` class with the attributes `make`, `model`, and `year`.

Write a method `get_descriptive_name`, which *returns* a neatly formatted descriptive name. For example, "1994 Chevy Lumina".

Use the `__str__` **Dunder/Magic** method to define the behavior for when `str()` is called on an instance of your class.

``` python
class Car:
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

Let's now work with the odometer to see how to add default values for an attribute and modify attributes through a method.

Add odometer_reading.

``` python
### Setting a Default Value for an Attribute

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        # --snip--
        self.odometer_reading = 0   # Added
    
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

While we can update the attributes directly, like above, you may want to write a method that updates that value for you. This way, you can implement logic that prevents intended behavior (e.g., rolling back the odometer).

``` python
class Car:
    # -- snip-- #
    
    def set_odometer(self, mileage):
        """Set the odometer reading to a given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

        
my_old_car = Car('chevy', 'lumina', 1994)

my_old_Car.set_odometer(10000)
my_old_car.read_odometer()

my_old_car.set_odometer(0)
```

### Exercise

Write a method `increment_odometer`, which takes one parameter `miles`, and increases the odometer by `miles`.

``` python
class Car:
    # -- snip-- #
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_old_car = Car('chevy', 'lumina', 1994)

my_old_car.increment_odometer(10)
my_old_car.read_odometer()
```

## Exercises

1. **Restaurant:** Make a class called  Restaurant. The  `__init__()` method for Restaurant should store two attributes: a restaurant_name and a `food_type`. Make a method called `describe_restaurant()` that prints these two pieces of information, and a method called `open_restaurant()` that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

    <details>
    <summary>Solution</summary>

    ```python
    class Restaurant:
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
    </details>
 <br>

2. **Number Served:** Start with your program from Exercise 1. Add an attribute called `number_served` with a default value of 0. Create an instance called `restaurant` from this class. Print the number of customers the restaurant has served, and then change this value and print it again.

    Add a method called `set_number_served()` that lets you set the number of customers that have been served. Call this method with a new number and print the value again.

    Add a method called `increment_number_served()` that lets you increment the number of customers who’ve been served.
    
    In reality, there is a capacity on the number of customers that can be served at once. So, add an attribute called `capacity` that has a default value of 100 (for backward-compatibility), or can be set upon instantiation. The `increment_number_served()` method should only update the `number_served` if the value passed is less than the `capacity`.
    
    Call this method with any number you like that could represent how many customers were served in, say, a day of business. Also, verify that number_served will only be incremented if the number served is below capacity.

    <details>
    <summary>Solution</summary>

    ```python
   class Restaurant:
       """A simple attempt to model a restaurant."""
       
       def __init__(self, restaurant_name, food_type, capacity=100):
           self.restaurant_name = restaurant_name
           self.food_type = food_type
           self.number_served = 0
           self.capacity = capacity

       def describe_restaurant(self):
           """Prints a description of the restaurant."""
           print(f"{self.restaurant_name.title()} serves {self.restaurant_type}.")
               
       def open_restaurant(self):
           """Opens the restaurant."""
           print(f"{self.restaurant_name.title()} is open!")
           
       def set_number_served(self, n):
           """Sets the number served to a specific value."""
           self.number_served = n

       def increment_number_served(self, n):
           """Increments the number served by a specific value, if possible."""
           if n < self.capacity:
               self.number_served += n
           else:
               print((f"{self.restaurant_name} has a capacity of {self.capacity}, and cannot serve that many people at once."))

   pizza_place = Restaurant("Palace Pizza", "pizza")

   print(f"pizza_place.number_served: {pizza_place.number_served}")
   pizza_place.number_served = 1
   print(f"pizza_place.number_served: {pizza_place.number_served}")

   pizza_place.set_number_served(10)
   print(f"pizza_place.number_served: {pizza_place.number_served}")

   pizza_place.increment_number_served(99)
   print(f"pizza_place.number_served: {pizza_place.number_served}")

   pizza_place.increment_number_served(999)
   print(f"pizza_place.number_served: {pizza_place.number_served}")

   # Verify the capacity can be set upon instantiation
   pasta_place = Restaurant("Olive Garden", "pasta", 500)
   print(f"pasta_place.capacity: {pasta_place.capacity}")
    ```
    </details>
 <br>


# Day X: Inheritence, Error Handling

# Day X: Algorithmic Complexity