
```

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