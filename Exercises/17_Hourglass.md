# Hourglass

## Starter Code

Start with the following code.

```python
def outer():
    ...

def edge():
    ...

def almost_middle():
    ...

def middle():
    ...

def build_hourglass():
    ...

def build_diamond():
    ...

##
## DO NOT CHANGE ANYTHING BELOW THIS LINE
##
build_hourglass()
print()
build_diamond()
```

Replace the `...` in the functions' bodies with `print` statements to build an hourglass and a diamond.

A function without a body will result in an error, so ellipses `...` are used as placeholder. This way development can occur without the Python interpreter raising errors.

Use functions to break up the problem into reusable blocks of code, **but do NOT change function names**.

## Desired Output
 
```text
#####
#   #
 # # 
  #  
 # # 
#   #
#####

  #  
 # # 
 # # 
  #  
```

<details>
<summary style="font-weight:bold">Solution</summary>
<br>

``` python
def outer():
    print("#####")

def edge():
    print("#   #")

def almost_middle():
    print(" # # ")

def middle():
    print("  #  ")

def build_hourglass():
    outer()
    edge()
    almost_middle()
    middle()
    almost_middle()
    edge()
    outer()

def build_diamond():
    middle()
    almost_middle()
    almost_middle()
    middle()

## DO NOT CHANGE ANYTHING BELOW THIS LINE
build_hourglass()
print()
build_diamond()
```

</details>
