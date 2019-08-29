from serial_j import SerialJ


class StrIPv4Data(SerialJ):
    schema = [
        {'name': 'prop1', 'type': (str, 'ipv4')}
    ]


valid_data = StrIPv4Data({'prop1': '172.16.255.1'})
print(valid_data)
# >>> {"prop1": "172.16.255.1"}

invalid_data = StrIPv4Data({'prop1': '172.16.256.1'})
# >>> ValueError: Property: 'prop1' with Value: '172.16.256.1' does not confirm with Type: (<class 'str'>, 'ipv4').
