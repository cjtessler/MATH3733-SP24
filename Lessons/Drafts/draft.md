

# Day X: Lists

## Lists

``` python
##### Lists #####
# Lists are used to store multipe items in a single variable.

### Grades...
## ...with variables
t1 = 100
t2 = 90
t3 = 70.5

## ...with lists
grades = [100, 90, 80]
print(grades)
print(grades[0])
print(grades[1:2])

### Add grades to the list
## Operations
grades = grades + [70, 60, 50] # concatenates list
print(grades)   # [100, 90, 80, 70, 60, 50]
grades *= 2     # concatenates a copy of the current list to the end
print(grades)   # [100, 90, 80, 70, 60, 50, 100, 90, 80, 70, 60, 50]

## Append Method
grades = [100, 80, 70]
grades.append(42)
print(grades)   # [100, 80, 70, 42]

grades[1] = 100	# list are mutable
print(grades)   # [100, 100, 80, 42]

## Wrong ways...
grades = grades.append(42)  # deletes current grade list
grades + [42]               # does not save new item
grades = grades + 42        # list concatenation requires two lists


### Iterating over a list
for grade in grades:
    print(grades)

### Exercise: Write a program that counts the number of A's, B's, C's, and failures in a list of grades. Use a 10-point scale.

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

### Use indexing when modifying elements
## Taxes
prices = [0.99, 14.95, 7.00]

# Undesired behavior
for p in prices: # makes a 'copy' of each element and stores it in p
    p *= 1.07
   
# notice prices haven't changed
print(prices) 	# [0.99, 14.95, 7.00]

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