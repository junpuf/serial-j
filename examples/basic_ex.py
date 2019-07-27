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
# >>> good apple

# ...and other fruits too.
print(fruits.orange)
# >>> very good orange
print(fruits.pineapple)
# >>> nice pineapple

# you can get the JSON formatted string back too.
print(fruits)
# >>> {"apple": "good apple", "orange": "very good orange", "pineapple": "nice pineapple"}

# interested to get the python dictionary back?
fruits_data = fruits.as_dict()
print(fruits_data)
# >>> {'apple': 'good apple', 'orange': 'very good orange', 'pineapple': 'nice pineapple'}
