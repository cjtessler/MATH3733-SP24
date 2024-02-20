
# Day 11: Dictionaries

## Initialization

[https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

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

eng2sp = {            Alternative declaration for readability
    'one': 'uno',
    'two': 'dos',
    'three': 'tres'
}

print(eng2sp)

# Access elements in a dictionary
print(eng2sp['two'])
print(eng2sp['four']) # KeyError
```

## Iteration

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

## Dictionary Comprehension

Use a dictionary comprehension to count the length of each word in a sentence.

```python
sentence = "The quick brown fox jumps over the lazy dog"
word_lengths = {}  # Initialize an empty dictionary

# Split the sentence into words and loop through each word
for word in sentence.split():
    word_lengths[word] = len(word)  # Set the word as key and its length as value in the dictionary

word_lengths = {word: len(word) for word in sentence.split()}
```

## Dictionaries as a Collection of Counter

 Suppose you are given a string and want to count how many times each letter appears.

``` python
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

h = histogram('parrot')
print(h)    # {"p": 1, "a": 1, "r": 2, "o": 1, "t": 1}

```

We can use the dictionary [`get`](https://www.w3schools.com/python/ref_dictionary_get.asp) method to simplify this program.

```python
def histogram(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

h = histogram('parrot')
print(h)    # {"p": 1, "a": 1, "r": 2, "o": 1, "t": 1}
```

## Exercise

1. Create a Contacts Dictionary
    - Start by creating an empty dictionary named `contacts`.
    - Add three contacts to the dictionary. Each contact should have a name as the key and their phone number as the value.

2. Add a New Contact.
    - Prompt the user to enter a new contact name and their phone number.
    - Check if the contact already exists in the dictionary. If it does, print a message saying the contact is already in the dictionary. Otherwise, add the new contact to the dictionary.
  
3. Update a Contact's Phone Number.
    - Prompt the user to enter the name of a contact whose phone number they want to update.
    - If the contact exists, prompt for the new phone number and update the contact's phone number in the dictionary. If the contact does not exist, print a message saying so.

4. Retrieve and Display a Contact's Phone Number.
    - Prompt the user to enter the name of a contact whose phone number they wish to retrieve.
    - Check if the contact exists in the dictionary. If it does, print the contact's name and phone number. If not, print a message indicating that the contact was not found.

5. Bonus: Display All Contacts.
    - Write a piece of code that prints all the contacts in the dictionary, formatted nicely. For example, each contact should be printed on a new line with the format: `Name: Phone Number`.
