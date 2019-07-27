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
# >>> {"apple": "good apple", "orange": "very good orange", "pineapple": "nice pineapple",
# >>> "snack": [{"cheese": "Feta", "chocolate": "Ferrero Rocher", "chips": []},
# >>>           {"chocolate": "Swiss milk chocolate", "chips":
# >>>                ["Cheetos", "Lays Classic Potato Chips", "Cool Ranch Doritos"]}]}