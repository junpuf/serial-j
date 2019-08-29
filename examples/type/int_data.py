from serial_j import SerialJ


class IntData(SerialJ):
    schema = [
        {'name': 'prop1', 'type': (int,)}
    ]


valid_data = IntData({'prop1': 1})
print(valid_data)
# >>> {"prop1": 1}
invalid_data = IntData({'prop1': "1"})
# >>> ValueError: Property: 'prop1' with Value: '1' does not confirm with Type: (<class 'int'>,).