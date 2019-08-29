from serial_j import SerialJ


class StrUUIDData(SerialJ):
    schema = [
        {'name': 'prop1', 'type': (str, 'uuid')}
    ]


valid_data = StrUUIDData({'prop1': '6a2b83e2-a5ae-4282-a814-1a4bb50ba3fb'})
print(valid_data)
# >>> {"prop1": "6a2b83e2-a5ae-4282-a814-1a4bb50ba3fb"}
valid_data = StrUUIDData({'prop1': '6a2b83e2a5ae4282a8141a4bb50ba3fb'})
print(valid_data)
# >>> {"prop1": "6a2b83e2a5ae4282a8141a4bb50ba3fb"}
valid_data = StrUUIDData({'prop1': '6a2b83e2a5ae-4282-a814-1a4bb50ba3fb'})
print(valid_data)
# >>> {"prop1": "6a2b83e2a5ae-4282-a814-1a4bb50ba3fb"}

invalid_data = StrUUIDData({'prop1': '6a2b83e2-a5ae-4282-814-1a4bb50ba3fb'})
# >>> ValueError: Property: 'prop1' with Value: '6a2b83e2-a5ae-4282-814-1a4bb50ba3fb' does not confirm with Type: (<class 'str'>, 'uuid').
