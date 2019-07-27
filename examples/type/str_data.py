from serial_j import SerialJ


class StrData(SerialJ):
    schema = [
        {'name': 'prop1', 'type': (str,)}
    ]


valid_data = StrData({'prop1': "str"})
print(valid_data)
# >>> {"prop1": 1}

invalid_data = StrData({'prop1': True})
print(invalid_data)
# >>> ValueError: Property: 'prop1' with Value: 'True' does not confirm with Type: (<class 'str'>,).
invalid_data = StrData({'prop1': 1})
print(invalid_data)
# >>> ValueError: Property: 'prop1' with Value: '1' does not confirm with Type: (<class 'str'>,).
