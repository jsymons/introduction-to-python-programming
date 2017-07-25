# Dictionaries

This unit will start dealing with more "advanced" data structures as dictionaries and sets. Dictionaries are a fundamental data structure in Python and in other programming languages. It's also referred as a [map or associative arrays (fancy term)](https://en.wikipedia.org/wiki/Associative_array). In Python, a Dictionary is from the type `dict` and curly braces `{}` are used to create dictionary literals:

```python
user = {
  'first_name': 'Tom',
  'last_name': 'Sawyer',
  'age': 12
}
```

The more traditional `dict` function can be used, although it's less clear and more verbose:

```python
user = dict([('first_name', 'Tom'), ('last_name', 'Sawyer'), ('age', 12)])
```

Think about a traditional dictionary (English, Spanish, etc). A dictionary "maps" words to their definitions:

```
"horse" > "a solid-hoofed plant-eating domesticated mammal with a flowing mane and tail..."
"dog" > "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, non-retractile claws, and a barking"
```

A Dictionary maps words to definitions, or more generally, **keys to values**. In the example of a traditional dictionary, the key is the word we're looking the definition for, and the value is the definition itself.

Python dictionaries are a generalization of this concept. We can map whatever keys to whatever values we want. Examples:

```python
todo_list = {
  'list_name': 'TODO list for Tom Sawyer',
  'todos': ['do the dishes', 'take out the trash', 'clean my room'],
  'date_limit': 'Monday July 24th'
}
```

In our example we have 3 keys (`'list_name'`, `'todos'` and `'date_limit'`) each one with its respective value. Python dicts support any type of value (as any other collection, they're heterogeneous):

```python
example_types = {
  'a_string': 'Hello World',
  'an_int': 23,
  'a_float': 3.1415,
  'a_boolean': True,
  'our_friend_none': None,
  'a_list': [2, 'a', 19.3],
  'a_tuple': (5, 3),
  'another dict!!': {
    'language': 'Python',
    'unit': 'Collections'
  }
}
```

Any valid Python data type is a valid value. But that doesn't apply to keys, they're way more restricted. Keys need to be of "hashable" types. We'll probably explain this during class, but what you need to know for now is that dict keys are usually strings or tuples. Try to create a dict with a `list` as a key and see how it fails with an ugly `"TypeError: unhashable type: 'list'"` error.

## Accessing dictionary values

Remember how to access elements in lists or tuples? With a list you access a particular element with the its "index" in the given list. If you have the list `['a', 'b', 'c']` and you want to access the element `'b'` you'd reference it by its position, in this case `1`. Lists are zero-indexed, that means that we have something like:

```python
my_python_list = ['a', 'b', 'c']
# Position:        0    1    2

print(my_python_list[1])  # b
```

Dictionaries are similar, but instead of getting implicit indexes from 0-N as lists, **WE are the ones stating the indexes...** in other words, the keys:

```python
user = {
  'first_name': 'Tom',
  'last_name': 'Sawyer',
  'age': 12
}

print(user['first_name'])  # Tom
print(user['age'])  # 12
```

The key in a dict will be the _entry point_ to the value stored. The same as a regular English dictionary. You search for the definition (**_value_**) using the word (**_key_**).

## Using Dictionaries

Once you've figure out how dictionaries work, how to create and access them, your next task is to interact and use them. A dictionary is another type of collection, so probably the first thing you want to do with it is to "iterate" over its elements. Example:

```python
user = {
  'first_name': 'Tom',
  'last_name': 'Sawyer',
  'age': 12
}
for key in user:
    print(key)

# >>> 'first_name'
# >>> 'last_name'
# >>> 'age'
```

From what we see in the previous example, what you get from the simple `for key in a_dictionary` is to iterate over all the keys. But what happens if you also want to access the values? Well, if you have the key, you can access the value:

```python
user = {
  'first_name': 'Tom',
  'last_name': 'Sawyer',
  'age': 12
}
for key in user:
    value = user[key]
    print(value)

# >>> 'Tom'
# >>> 'Sawyer'
# >>> 12
```

Trying to iterate over dictionary's values is a **really** common task and the Python guys and gals have thought about it and included a method to simplify our lives...

## Dictionary methods

Dictionary have many interesting methods that will help us in our day to day job; to complete our previous example we can use the `values` method to get the values directly without having to manually access them using the key (compare this example to the previous one):

```python
user = {
  'first_name': 'Tom',
  'last_name': 'Sawyer',
  'age': 12
}
for value in user.values():
    print(value)

# >>> 'Tom'
# >>> 'Sawyer'
# >>> 12
```

We can also get both, keys and values at the same time with the `items` method:

```python
user = {
  'first_name': 'Tom',
  'last_name': 'Sawyer',
  'age': 12
}
for key, value in user.items():
    print("{}: {}".format(key, value))

# >>> first_name: 'Tom'
# >>> last_name: 'Sawyer'
# >>> age: 12
```

Let me finish this section saying this: there are **MANY** more methods in a dict that are incredibly useful for our day to day job. Sadly, we won't cover all of them, so the [official documentation](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) ([also for Python 2](https://docs.python.org/2/library/stdtypes.html#mapping-types-dict)) should be your second home.

## Extra readings about dicts:

* Dive Into Python 3 has a great intro to [dictionaries](http://www.diveintopython3.net/native-datatypes.html#dictionaries).
* Automate the Boring Stuff goes a little bit deeper in [Chapter 5](https://automatetheboringstuff.com/chapter5/).
