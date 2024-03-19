# Day X: Inheritance

## Inheritance

Review slide 8 at https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/mit6_0001f16_lec9/.

If the class we are writing is a specialized version of another class we already wrote, we can use **inheritance**. The original class is the **parent class**, and the new class is the **child class**. The child class can inherit any or all of the attributes of its parent class, and is free to define new attributes and methods of its own.

Let's write a child class for our `Car` class:

```python
class Car:
    """A simple attempt to model a var."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"
    
    def get_odometer(self):
        return self.odometer_reading
    
    def set_odometer(self, miles):
        """Set the odometer reading to a given value.
        Reject the change if it attempts to roll back the odometer."""
        if self.odometer_reading >= miles:
            print("We can roll back the odometer!")
        else:
            self.odometer_reading = miles

    def increment_odometer(self, miles):
        self.odometer_reading += miles
```

An electric car is a specialized car, so let's write it as a child class by doing the following:

- Put the name of the parent class in parentheses in the class definition
- Call the `__init__` method of the parent class using the `super()` function.

```python
class ElectricCar(Car):
    """Represents aspects of a car, specific  to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of your parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('Tesla', 'Model Y', 2024)
print(my_tesla)
```

Now, let's add an attribute specific to electric cars: a battery.

```python
class ElectricCar(Car):

    def __init__(self, make, model, year):
        self.battery_size = 60

    def describe_battery(self):
        """Print battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla.describe_battery()
```

### Exercise

Add an attribute to the `Car` class called `wheels` with a default value of 4, which specifies the number of wheels on a car.

Write a `Motorcycle` class that inherits from `Car` which changes the values of `wheels` to 2 during its initialization.

Write a method `describe_wheels` for the parent class that prints how many wheels the vehicle has.

Instantiate the child class and call the method inherited from the parent class.

<details>
<summary>Solution</summary>

```python
class Car:
    def __init__(self, make, model, year):
        self.wheels = 4

    def describe_wheels(self):
        print(f"This car has {self.wheels} wheels.")

class Motorcycle(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) 
        self.wheels = 2

my_bike = Motorcycle("Harley Davidson", "Road Glide", 2024)
print(my_bike)
my_bike.describe_wheels()
```
</details>

### Overriding Methods

A child can override methods from its parent class. For example, an electric car does not have a gas tank.

```python
class Car:
    def __init__(self, make, model, year):
        self.gas_tank = 100

    def get_gas_tank(self):
        print(f"The gas tank is at {self.gas_tank}%.")


class ElectricCar(Car):
    def get_gas_tank(self):
        print("This car does not have a gas tank.")

my_tesla.get_gas_tank()
```

### Exercise

For `Motorcycle`, override the `describe_wheels` method from the parents class so that it prints "bike" instead of "car".

<details>
<summary>Solution</summary>

```python
class Motorcycle(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) 
        self.wheels = 2

    def describe_wheels(self):
        print(f"This bike has {self.wheels} wheels.")

my_bike = Motorcycle("Harley Davidson", "Road Glide", 2024)
print(my_bike)
my_bike.describe_wheels()
```

Note that it would likely be better to generalize the parent class to say "vehicle". Alternately, we could write `Motorcycle` has its own class or write a general `Vehicle` class and inherit from that.

</details>

### Modules

In order to keep projects organized, you can store classes in **modules** and then import the classes you need into your main program.

```python
# main.py

from car import Car
my_new_car = Car('nissan', 'versa', 2010)
print(my_new_car)
```

Notice that commands not in the class are run. To prevent this, use the following paradigm when developing modules:

```python
if __name__ == "__main__":
    # logic for module
```

You can import the entire module using `*`, although this is not considered best practice. This could lead to unexpected behavior where the imported module overrides a function or method already in use (naming collection).

```python
# main.py

from car import *
my_new_car = Car('nissan', 'versa', 2010)
print(my_new_car)

my_electric_car = ElectricCar("nissan", "leaf", 2004)
print(my_electric_car)
```

Instead, simply import the module and use dot notation to access the classes.

```python
# main.py
import car

my_mustang = car.Car('Ford', 'Mustang', 2024)
my_bike = car.Motorcycle('Honda', 'Rebel', 2024)
```

You can use **aliases** to have you own shorthand for imported classes.

```python
import car as c
from car import ElectricCar as EC

my_mustang = c.Car('Ford', 'Mustang', 2024)
my_electric_car = EC("nissan", "leaf", 2004)
```

## Exercise

1. **Ice Cream Stand:** An ice cream stand is a specific kind of restaurant. Write a class called `IceCreamStand` that inherits from the `Restaurant` class you wrote previously. Add an attribute called `flavors` that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of `IceCreamStand`, and call this method.

   <details>
   <summary>Solution</summary>

   ```python
   TODO
   ```
   </details>

<br>

2. **Importing:** Import `IceCreamStand` into `main.py` and create an instance.

   <details>
   <summary>Solution</summary>

   ```python
   TODO
   ```
   </details>