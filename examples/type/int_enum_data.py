from serial_j import SerialJ


class IntEnumerationData(SerialJ):
    schema = [
        {'name': 'prop2', 'type': (int, (1, 64, 343))}
    ]


valid_data = IntEnumerationData({'prop2': 1})
print(valid_data)
# >>> {"prop1": 1}
valid_data = IntEnumerationData({'prop2': 64})
print(valid_data)
# >>> {"prop1": 64}
valid_data = IntEnumerationData({'prop2': 343})
print(valid_data)
# >>> {"prop1": 343}

invalid_data = IntEnumerationData({'prop2': "1"})
# >>> ValueError: Property: 'prop2' with Value: '1' does not confirm with Type: (<class 'int'>, (1, 64, 343)).
invalid_data = IntEnumerationData({'prop2': 2})
# >>> ValueError: Property: 'prop2' with Value: '2' does not confirm with Type: (<class 'int'>, (1, 64, 343)).
