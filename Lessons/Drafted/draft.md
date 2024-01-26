# Day X: Scope

### Scope

Called a function creates a new **scope**, which is also referred to as a **frame**.

Use [Python Tutor](https://pythontutor.com/visualize.html#mode=edit) to visualize scope.

``` python
def f(x): # name x used as parameter 
    y = 1 
    x = x + y 
    print('x =', x) 
    return x 
    
x = 3 
y = 2 
z = f(x) # value of x used as argument
print('z =', z) 
print('x =', x) 
print('y =', y) 
```

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

### `global`

TODO

# Day X: Recursion

## Recursion

The Fibonacci sequence is 1, 1, 2, 3, 5, 8, 13, 21, 34,...

How can a program compute this sequence?

`fib(1) == 1` and `fib(2) == 1` are the base cases, and the next numbers are the sum of the prevous two.

Recursion is the process of repeating items in a self-similar way.

![https://res.cloudinary.com/practicaldev/image/fetch/s--KA7Ky3uR--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/226xc0p9pgtgadnin92j.jpeg](https://res.cloudinary.com/practicaldev/image/fetch/s--KA7Ky3uR--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/226xc0p9pgtgadnin92j.jpeg)

## What is recursion?

Algorithmically, we design solutions to problem by **divide-and-conquer**. That is, reduce a problem to simpler versions of the same problem.

Semantically, we write a function that calls itself.

- We want to avoid infinite recursion
  - We must have one or more base cases that are easy to solve.
  - We must solve the same problem on some other input with the goal of simplifying the larger problem input.

## Iterative Algorithms

Looping constructs such as `while` and `for` loops lead to iterative algorthms.

Capture computation is a set of **state variables** can update on each iteration of the loop. 

## Multiplication - Iterative

`a` is added to itself `b` times: `a*b = a + a + a + ... + a + a`


``` python
def mult_iter(a, b):
    result = 0          # state variable
    while b > 0:        # iteration
        result += a     # current value of computation, a running sum
        b -= 1          # current value of iteration variable
    return result
```

## Multiplication - Recursive

Recursive step: How to reduce problem to a simpler/small version of the same problem.

`a*b = a + (a + a + ... + a) = a + [a * (b - 1)]

The brackets show the recursive reduction.

Base case: Keep reducing the problem until a we reach a simple case that can be solved directly.

If `b = 1`, then `a*b = a`.

``` python
def mult(a, b):
    if b == 1:      # base case
        return a
    else:
        return a + mult(a, b-1)
```

## Factorial

`n! = n * (n-1) * (n-2) * ... * 2 * 1`

``` python 
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

[Python Tutor](https://pythontutor.com/visualize.html#code=def%20factorial%28n%29%3A%0A%20%20%20%20if%20n%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20n%20*%20factorial%28n-1%29%0A%20%20%20%20%20%20%20%20%0Aprint%28factorial%286%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Observation

Each recursive call to a function creates its own scope.

Flow of control passes back to previous scope once a function call returns the value.

## Recursion with Multiple Base Cases (Fibonacci)

Base cases: `fib(1) == 1` and `fib(2) == 1`
Recursive case: `fib(n) = fib(n-1) + fib(n-1)`

``` python
# Inefficient Fibonacci
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-1)

print(fib(10))
print(fib(34))  # 11,405,774 recursive calls to the function
```

Correctness follows from mathematical induction.

How can this computation's efficieny be improved?

[Fibonacci Visualization 6:25 - 11:00](https://youtu.be/oBt53YbR9Kk?t=384)

The time complexity is `2^n` (exponential).

Notice that there is repeated computations. The algorithm can "remember" computations by using a technique known as **memoization**.

More on time complexity and memoization later.

# Day X: Strings

## Strings

A string is a sequence of characters.

## Indexing

``` python
## The "index" is a location in a string.
## Python strings are zero indexed (the first character is at index 0)
# positive indexing
fruit = 'banana'
letter = fruit[1]
print(letter) # prints 'a'
# the expression in the bracket is the index, it begins at 0
print(fruit[0]) # prints 'b'

# indexing backwards
print(fruit[-1]) # prints 'a'
print(fruit[-4]) # prints 'n'
```

## `len()`

``` python
length = len(fruit)	# careful to not use len as variable
print(length) # prints 6
print(fruit[length]) # IndexError: string index out of range
print(fruit[length-1]) # prints 'a'
```

## Iteration (String transversal)

``` python
## transversal with a while loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1
    
## transversal with a for loop
for index in range(len(fruit)):
    print(fruit[index]
          
# If we do not need the index, we can iterate through the characters directly         
for ch in fruit:
    print(ch)

# If we need the index and don't like range(len(fruit))
# use enumerate (this is considered "pythonic")
for i, ch in enumerate(fruit):
    print(i, ch)
```

## Pythonic

``` python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## String Slicing

``` python
s = 'Monty Python'
first = s[0:5] 
print(first) # prints 'Monty'
# 0 <= i < 5

second = s[6:12]
print(second) # prints 'Python'

print(s[:3]) # prints 'Mon'
# if no starting index is given, defaults to 0
print(s[10:]) # prints 'on'

# Exercise: Print the space
print(s[5:6])
```

# Day X: More on Strings

## Immutability

Strings are immutable, which means they CANNOT be changed once defined.

``` python
# immutable == can't change
greeting = 'Hello, world!'

# Change the first letter to a J
greeting[0] = 'J' # TypeError: 'str' object does not support item reassignment
greeting = 'J' + greeting[1:]
```

## Searching

``` python
### Searching
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

print(find('banana', 'n')) # prints 2
print(find('banana', 'h')) # prints -1

# Exercise: Generalize the function so that it has a third parameter, the index in the word where it should start looking
def indexed_find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

print(indexed_find('banana', 'n', 3)) # prints 4
print(indexed_find('banana', 'h', 3)) # prints -1
```

## Looping and Counting

``` python
## Looping and Counting
counter = 0
for letter in 'banana':
    if letter == 'a':
        counter += 1
print(counter) # prints 2

# Exercise: Encapsulate this logic into a function called count
def count(word, l):
    counter = 0
    for letter in word:
        if letter == l:
            counter += 1
     return counter
 
print(count('banana', 'a')) # prints 2
```

## Escape Characters

``` text
>>> print("We are the so-called "Vikings" from the north.")
  File "<stdin>", line 1
    "We are the so-called "Vikings" from the north."
                           ^
SyntaxError: invalid syntax

>>>  print("We are the so-called \"Vikings\" from the north.")
We are the so-called "Vikings" from the north.

>>> print("The only problem\nwith haiku is you just get\nstarted and then you")
The only problem
with haiku is you just get
started and then you
```

## String Methods

``` python
# https://docs.python.org/3/library/stdtypes.html#string-methods
word = 'banana'

# upper
new_word = word.upper() # we are 'invoking' upper on word
print(new_word) # prints 'BANANA'
print(word) # string methods do not change the string, they return a new string

# find
index = word.find('a')
print('a is at index', index)

# this function is more general that ours
index = word.find('na')
print('na begins at index', index)

# Exercise: Peruse the string methods in the docs. What does strip and replace do?
word = "help!!!!!!!!!!!!"
print(word.rstrip('!')) # prints 'help'
print(word.replace('!', '.'))

# isX methods return a Boolean
'1'.isalpha() # False
'1'.isdigit() # True
'a'.islower() # True
'A'.isupper() # True
```

## Comparison

``` python
# The 'in' operator
print('a' in 'banana') # True
print('l' in 'banana') # False


# comparison
print('A' == 'a') # False
print('A' < 'a')  # True

# order
# http://www.asciichart.com/
print(ord('A'))	# 65
print(ord('a'))	# 97
print('#' < 'a') # True. why?

# chr
print(chr(65)) # A
print(chr(97)) # a
```

## Star Wars ASCII

[https://youtu.be/Dgwyo6JNTDA](https://youtu.be/Dgwyo6JNTDA)

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