# Serial-J
Serializing JSON data into Python object with minimal effort.

## Example
Let's first see a basic example.

```python
from serial_j import SerialJ

class FruitBucket(SerialJ):
    # define how our data should look like using `schema`.
    schema = [
        {
            'name': 'apple',
            'optional': False,
            'nullable': False,
            'is_compound': False,
            'compound_serializer': None,
        },
        {
            'name': 'orange',
            'optional': False,
            'nullable': False,
            'is_compound': False,
            'compound_serializer': None,
        },
        {
            'name': 'pineapple',
            'optional': False,
            'nullable': False,
            'is_compound': False,
            'compound_serializer': None,
        },
    ]

# test data for FruitBucket 
test1 = dict(
    apple="good apple",
    orange="very good orange",
    pineapple="nice pineapple",
)

# serialize `test1` into `FruitBucket` object
fruits = FruitBucket(test1)

# `fruits` is a proper python object , which means that you can use 
# `fruits.apple` syntax to retrieve the value of `apple`.
print(fruits.apple)
>>> good apple

# ...and other fruits too.
print(fruits.orange)
>>> very good orange
print(fruits.pineapple)
>>> nice pineapple

# you can get the JSON formatted string back too.
print(fruits)
>>> {"apple": "good apple", "orange": "very good orange", "pineapple": "nice pineapple"}

# interested to get the python dictionary back?
fruits_data = fruits.as_dict()
print(fruits_data)
>>> {'apple': 'good apple', 'orange': 'very good orange', 'pineapple': 'nice pineapple'}
```

That's ok. 
But, we can do more than just that. Let's see how we can serialize more complex data structure into python object with another example.

```python
from serial_j import SerialJ

class Snack(SerialJ):
    schema = [
        # cheese is nice but is optional.
        {
            'name': 'cheese',
            'optional': True,
            'nullable': False,
            'is_compound': False,
            'compound_serializer': None,
        },
        # chocolate is a MUST have.
        {
            'name': 'chocolate',
            'optional': False,
            'nullable': False,
            'is_compound': False,
            'compound_serializer': None,
        },
        # chips is a must but we have to decide which kind later, 
        # so its value can be None, False, "", {}, [].
        {
            'name': 'chips',
            'optional': False,
            'nullable': True,
            'is_compound': False,
            'compound_serializer': None,
        },
    
    ]


class NestedBucket(SerialJ):
    schema = [
        {
            'name': 'apple',
            'optional': False,
            'nullable': False,
            'is_compound': False,
            'compound_serializer': None,
        },
        {
            'name': 'orange',
            'optional': False,
            'nullable': False,
            'is_compound': False,
            'compound_serializer': None,
        },
        {
            'name': 'pineapple',
            'optional': False,
            'nullable': False,
            'is_compound': False,
            'compound_serializer': None,
        },
        {
            'name': 'snack',
            'optional': False,
            'nullable': False,
            'is_compound': True,
            'compound_serializer': Snack,
        }
    ]
    
# test data for NestedBucket
test2 = dict(
    apple="good apple",
    orange="very good orange",
    pineapple="nice pineapple",
    snack=dict(
        chocolate="Ferrero Rocher",
        chips=[] # yeah its a list of chips!
    ),
)

my_snacks = NestedBucket(test2)
print(my_snacks)
>>> {"apple": "good apple", "orange": "very good orange", "pineapple": "nice pineapple", "snack": {"chocolate": "Ferrero Rocher", "chips": []}}
```

## To be continued...
