from serial_j import SerialJ


class FloatData(SerialJ):
    schema = [
        {'name': 'prop1', 'type': (float,)}
    ]


valid_data = FloatData({'prop1': 1.0})
print(valid_data)
# >>> {"prop1": 1.0}

invalid_data = FloatData({'prop1': "1.1"})
# >>> ValueError: Property: 'prop1' with Value: '1.1' does not confirm with Type: (<class 'float'>,).
