from serial_j import SerialJ


class StrIPv6Data(SerialJ):
    schema = [
        {'name': 'prop1', 'type': (str, 'ipv6')}
    ]


valid_data = StrIPv6Data({'prop1': '2001:0db8:0a0b:12f0:0000:0000:0000:0001'})
print(valid_data)
# >>> {"prop1": "2001:0db8:0a0b:12f0:0000:0000:0000:0001"}
valid_data = StrIPv6Data({'prop1': '684D:1111:222:3333:4444:5555:6:77'})
print(valid_data)
# >>> {"prop1": "684D:1111:222:3333:4444:5555:6:77"}

invalid_data = StrIPv6Data({'prop1': '2001:0db8:0a0b:12f0:00000:0000:0001'})
# >>> ValueError: Property: 'prop1' with Value: '2001:0db8:0a0b:12f0:00000:0000:0001' does not confirm with Type: (<class 'str'>, 'ipv6').
