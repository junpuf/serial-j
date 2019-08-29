from serial_j import SerialJ


class IntLambdaData(SerialJ):
    schema = [
        {'name': 'prop4', 'type': (int, lambda x: x % 2 == 0)}
    ]


valid_data = IntLambdaData({'prop4': 2})
print(valid_data)
# >>> {"prop4": 2}

invalid_data = IntLambdaData({'prop4': 1})
# >>> ValueError: Property: 'prop4' with Value: '1' does not confirm with Type: (<class 'int'>, <function IntLambdaData.<lambda> at 0x104af6e18>).
