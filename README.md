[![https://github.com/JunpuFan/serial-j](https://github.com/JunpuFan/static/blob/master/logo.png)](https://github.com/JunpuFan/serial-j)

<p align="center">
  <img width="620" height="422" src="https://github.com/JunpuFan/static/blob/master/demo1.gif">
</p>

## Features 
   1. Serialize JSON / Python Dictionary data into Python object based on a compact data `schema`.
       1. Data `schema` is a python list `[]` of many `{}`.
       2. Each `{}` in the `schema` defines a property in your `JSON` data. 
       3. The easiest form of a property definition is `{'name':'my_property'}` which means:
          1. Your `JSON` data **MUST** contain a property called `my_property` .
          2. Its value **MUST** be a **non-empty** value. 
          3. Non-empty means that the value of  `my_property` can not be `None`, `""`, `()`, `[]`, or `{}`.
       4. Additional options are available to give you more control over your data definition. Those options are: `nullable`, `optional`, `is_compound`, `compound_serializer`, `compound_schema` and `type`.
          1. Option `nullable: True` means the value of `my_property` can be `None`.
          2. Option `optional: True` means `my_property` may or may not exist in your `JSON` data.
             1. In case `my_property` exist, verify all applicable options.
             2. In case `my_property` doesn't exist, we ignore `my_property`.
          3. Option `is_compound: True` means `my_property` is a nested `JSON` object or an Array of `JSON` objects.
             1. When `is_compound: True`, you must provide either `compound_serializer` or `compound_schema` so we can property serialize this nested data structure.
                1. `compound_serializer` is a `SerialJ` serializer class.
                2. `compound_schema` has the same structure as the data `schema`.
          4. Option `type` gives you the power to validate the value of each property in your `JSON` data. Currently supported type definitions are:
             1. `'type': (bool,)` a boolean value.
             2. `'type': (float,)` a floating point number.
             3. `'type': (int,)` an integer.
             4. `'type': (int, (1, 64, 343))` an enumeration of integers, this means that the value of a `JSON` property should be in `(1, 64, 343)`.
             5. `'type': (int, range(1, 10, 3)`, a range of integers, this means that the value of a `JSON` property should be in `range(1, 10, 3)`.
             6. `'type': (int, lambda x: x % 2 == 0)` a user defined `lambda` expression used to filter desired integer values, the above example `lambda`  specifies the value of the `JSON` property should be a `even` number.
             7. `'type': (str,)` a string value.
             8. `'type': (str, ('SUCCESS', 'FAILURE'))` an enumeration of strings, this means that the value of a `JSON` property should be in `('SUCCESS', 'FAILURE')`. Note that `('SUCCESS', 'FAILURE')` is just an example here, you can define anything you like.
             9. `'type': (str, 'email')` an email address.
             10. `'type': (str, 'url')` a web url.
             11. `'type': (str, 'ipv4')` an IPv4 address.
             12. `'type': (str, 'ipv6')` an IPv6 address.
             13. `'type': (str, 'uuid')` an UUID string.
             14. `'type': (str, '[^@]+@[^@]+\.[^@]+')` a user defined `regex`. 
   2. Automatically validate every JSON properties defined in the `schema` based on varies additional options specified in `schema`.
   3. You are given convenient built-in methods that you can use to convert your data back to JSON encoded string or JSON / Python Dictionary.
   4. You have the flexibility of defining additional methods in your serializer class that utilize your data in anyway you want.



## Example Codes

| Name                                                  | Code                                                         |
| ----------------------------------------------------- | ------------------------------------------------------------ |
| Basic Example                                         | [basic_ex.py](https://github.com/JunpuFan/serial-j/blob/master/examples/basic_ex.py) |
| Serialize Nested Json Data with `compound_schema`     | [nested_ex2.py](https://github.com/JunpuFan/serial-j/blob/master/examples/nested_ex2.py) |
| Serialize Nested Json Data with `compound_serializer` | [nested_ex1.py](https://github.com/JunpuFan/serial-j/blob/master/examples/nested_ex1.py) |
| Data Type Validation: all in one example              | [typed_ex.py](https://github.com/JunpuFan/serial-j/blob/master/examples/typed_ex.py) |
| Data Type Validation: `bool`                          | [bool_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/bool_data.py) |
| Data Type Validation: `float`                         | [float_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/float_data.py) |
| Data Type Validation: `int`                           | [int_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/int_data.py) |
| Data Type Validation: `int enum`                      | [int_enum_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/int_enum_data.py) |
| Data Type Validation: `int range`                     | [int_ranged_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/int_ranged_data.py) |
| Data Type Validation: `int lambda`                    | [int_lambda_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/int_lambda_data.py) |
| Data Type Validation: `str`                           | [str_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/str_data.py) |
| Data Type Validation: `str enum`                      | [str_enum_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/str_enum_data.py) |
| Data Type Validation: `str email`                     | [str_email_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/str_email_data.py) |
| Data Type Validation: `str url`                       | [str_url_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/str_url_data.py) |
| Data Type Validation: `str uuid`                      | [str_uuid_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/str_uuid_data.py) |
| Data Type Validation: `str ipv4`                      | [str_ipv4_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/str_ipv4_data.py) |
| Data Type Validation: `str ipv6`                      | [str_ipv6_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/str_ipv6_data.py) |
| Data Type Validation: `str regex`                     | [str_regex_data.py](https://github.com/JunpuFan/serial-j/blob/master/examples/type/str_regex_data.py) |



## Basic Example
Let's first see a basic example. 

```python
from serial_j import SerialJ

class FruitBucket(SerialJ):
    # define how our data should look like using `schema`.
    schema = [
        {'name': 'apple'},
        {'name': 'orange'},
        {'name': 'pineapple'},
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



## Nested JSON Data 

Let's see how we can serialize more complex data structure into python object.



##### Serializing Nested JSON Data with `compound_schema`.

Define a nested data `schema` called `compound_schema` to serialize nested `JSON` data.

```python
from serial_j import SerialJ

class SnackBucket(SerialJ):
    schema = [
        {'name': 'apple'},
        {'name': 'orange'},
        {'name': 'pineapple'},
        {'name': 'snack', 'is_compound': True,
            'compound_schema': [
                 {'name': 'cheese', 'optional': True},
                 {'name': 'chocolate'},
                 {'name': 'chips', 'nullable': True},
            ],
        },
    ]

test3 = dict(
    apple="good apple",
    orange="very good orange",
    pineapple="nice pineapple",
    snack=[
        dict(
            cheese="Feta",
            chocolate="Ferrero Rocher",
            chips=[] 
        ),
        dict(
            chocolate="Swiss milk chocolate",
            chips=["Cheetos", "Lays Classic Potato Chips", "Cool Ranch Doritos"] 
        ),
    ]
)
mysnacks = SnackBucket(test3)
print(mysnacks)
>>> {"apple": "good apple", "orange": "very good orange", "pineapple": "nice pineapple", 
>>> "snack": [{"cheese": "Feta", "chocolate": "Ferrero Rocher", "chips": []}, 
>>>           {"chocolate": "Swiss milk chocolate", "chips": 
>>>                ["Cheetos", "Lays Classic Potato Chips", "Cool Ranch Doritos"]}]}
```



##### Serializing Nested JSON Data with `compound_serializer`.

Define a separete data `SerialJ` serializer called `compound_serializer` to serialize nested `JSON` data.

```python
from serial_j import SerialJ
class Snack(SerialJ):
    schema = [
        # cheese is nice but is optional.
        {'name': 'cheese', 'optional': True},
        # chocolate is a MUST have.
        {'name': 'chocolate'},
        # chips is a must but we have to decide which kind later, 
        # so its value can be None, False, "", {}, [].
        {'name': 'chips', 'nullable': True},
    ]
    
class NestedBucket(SerialJ):
    schema = [
        {'name': 'apple'},
        {'name': 'orange'},
        {'name': 'pineapple'},
        {'name': 'snack', 'is_compound': True, 'compound_serializer': Snack}
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
>>> {"apple": "good apple", "orange": "very good orange", "pineapple": "nice pineapple", 
>>>  "snack": {"chocolate": "Ferrero Rocher", "chips": []}}
```



## Data Type Validation 

a compact example that shows all data types currently suppoted by this package.

```python
from serial_j import SerialJ


class TypedData(SerialJ):
    schema = [
        {'name': 'prop1', 'type': (int,)},
        {'name': 'prop2', 'type': (int, (1, 64, 343))},
        {'name': 'prop3', 'type': (int, range(1, 10, 3))},
        {'name': 'prop4', 'type': (int, lambda x: x % 2 == 0)},
        {'name': 'prop5', 'type': (str,)},
        {'name': 'prop6', 'type': (str, ('SUCCESS', 'FAILURE'))},
        {'name': 'prop7', 'type': (str, 'email')},
        {'name': 'prop8', 'type': (str, 'url')},
        {'name': 'prop9', 'type': (str, 'ipv4')},
        {'name': 'prop10', 'type': (str, 'ipv6')},
        {'name': 'prop11', 'type': (str, 'uuid')},
        {'name': 'prop12', 'type': (str, '[^@]+@[^@]+\.[^@]+')},
        {'name': 'prop13', 'type': (float,)},
        {'name': 'prop14', 'type': (bool,)},
    ]


test1 = {
    'prop1': 1,
    'prop2': 64,
    'prop3': 4,
    'prop4': 2,
    'prop5': "str",
    'prop6': 'SUCCESS',
    'prop7': 'anyone@emailservice.com',
    'prop8': 'https://www.something.com/something-something/something/12345',
    'prop9': '172.16.255.1',
    'prop10': '2001:0db8:0a0b:12f0:0000:0000:0000:0001',
    'prop11': 'c026dd66-86f2-498e-8c2c-858179c0c93d',
    'prop12': 'junpufan@me.com',
    'prop13': 0.1,
    'prop14': True
}

data1 = TypedData(test1)
print(data1)
# >>> {"prop1": 1, "prop2": 64, "prop3": 4, "prop4": 2, "prop5": "str",
# >>> "prop6": "SUCCESS", "prop7": "anyone@emailservice.com",
# >>> "prop8": "https://www.something.com/something-something/something/12345",
# >>> "prop9": "172.16.255.1", "prop10": "2001:0db8:0a0b:12f0:0000:0000:0000:0001",
# >>> "prop11": "c026dd66-86f2-498e-8c2c-858179c0c93d", "prop12": "junpufan@me.com",
# >>> "prop13": 0.1, "prop14": true}

```

