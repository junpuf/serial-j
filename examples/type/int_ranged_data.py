from serial_j import SerialJ


class IntRangedData(SerialJ):
    schema = [
        {'name': 'prop3', 'type': (int, range(1, 10, 3))}
    ]


valid_data = IntRangedData({'prop3': 1})
print(valid_data)
# >>> {"prop3": 1}
valid_data = IntRangedData({'prop3': 4})
print(valid_data)
# >>> {"prop3": 4}
valid_data = IntRangedData({'prop3': 7})
print(valid_data)
# >>> {"prop3": 7}

invalid_data = IntRangedData({'prop3': 2})
# >>> ValueError: Property: 'prop3' with Value: '2' does not confirm with Type: (<class 'int'>, range(1, 10, 3)).
invalid_data = IntRangedData({'prop3': 10})
# >>> ValueError: Property: 'prop3' with Value: '10' does not confirm with Type: (<class 'int'>, range(1, 10, 3)).
