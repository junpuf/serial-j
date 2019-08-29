from serial_j import SerialJ, create_schema


class SnackBucket(SerialJ):
    schema = create_schema([
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
    ])


test3 = dict(
    apple="good apple",
    orange="very good orange",
    pineapple="nice pineapple",
    banana1="banana",
    banana2="banana",
    banana3="banana",
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
    ],
    snack1=[],
    snack2=[],

)
mysnacks = SnackBucket(test3)
print(mysnacks)
# >>> {"apple": "good apple", "orange": "very good orange", "pineapple": "nice pineapple",
# >>> "snack": [{"cheese": "Feta", "chocolate": "Ferrero Rocher", "chips": []},
# >>>           {"chocolate": "Swiss milk chocolate", "chips":
# >>>                ["Cheetos", "Lays Classic Potato Chips", "Cool Ranch Doritos"]}]}
