from serial_j import SerialJ


class StrEnumerationData(SerialJ):
    schema = [
        {'name': 'prop1', 'type': (str, ('SUCCESS', 'FAILURE'))}
    ]


valid_data = StrEnumerationData({'prop1': "SUCCESS"})
print(valid_data)
# >>> {"prop1": "SUCCESS"}
valid_data = StrEnumerationData({'prop1': "FAILURE"})
print(valid_data)
# >>> {"prop1": "FAILURE"}

invalid_data = StrEnumerationData({'prop1': "HELLO WORLD"})
# >>> ValueError: Property: 'prop1' with Value: 'HELLO WORLD' does not confirm with Type: (<class 'str'>, ('SUCCESS', 'FAILURE')).
invalid_data = StrEnumerationData({'prop1': 1})
# >>> ValueError: Property: 'prop1' with Value: '1' does not confirm with Type: (<class 'str'>, ('SUCCESS', 'FAILURE')).
