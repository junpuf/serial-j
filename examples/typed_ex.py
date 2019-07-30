from serial_j import SerialJ
from uuid import UUID

class TypedData(SerialJ):
    schema = [
        {'name': 'prop1', 'type': (int,)},
        {'name': 'prop2', 'type': (int, (1, 64, 343))},
        {'name': 'prop3', 'type': (int, range(1, 10, 3))},
        {'name': 'prop4', 'type': (int, lambda x: x % 2 == 0)},
        {'name': 'prop5', 'type': (str,)},
        {'name': 'prop6', 'type': (str, ('SUCCESS', 'FAILURE'))},
        {'name': 'prop7', 'type': (str, 'email')},
        {'name': 'prop8', 'type': (str, 'url')},
        {'name': 'prop9', 'type': (str, 'ipv4')},
        {'name': 'prop10', 'type': (str, 'ipv6')},
        {'name': 'prop11', 'type': (str, 'uuid')},
        {'name': 'prop12', 'type': (str, '[^@]+@[^@]+\.[^@]+')},
        {'name': 'prop13', 'type': (float,)},
        {'name': 'prop14', 'type': (bool,)},
    ]


test1 = {
    'prop1': 1,
    'prop2': 64,
    'prop3': 4,
    'prop4': 2,
    'prop5': "str",
    'prop6': 'SUCCESS',
    'prop7': 'anyone@emailservice.com',
    'prop8': 'https://www.something.com/something-something/something/12345',
    'prop9': '172.16.255.1',
    'prop10': '2001:0db8:0a0b:12f0:0000:0000:0000:0001',
    'prop11': UUID('c026dd66-86f2-498e-8c2c-858179c0c93d'),
    'prop12': 'junpufan@me.com',
    'prop13': 0.1,
    'prop14': True
}

data1 = TypedData(test1)
print(data1)
# >>> {"prop1": 1, "prop2": 64, "prop3": 4, "prop4": 2, "prop5": "str",
# >>> "prop6": "SUCCESS", "prop7": "anyone@emailservice.com",
# >>> "prop8": "https://www.something.com/something-something/something/12345",
# >>> "prop9": "172.16.255.1", "prop10": "2001:0db8:0a0b:12f0:0000:0000:0000:0001",
# >>> "prop11": "c026dd66-86f2-498e-8c2c-858179c0c93d", "prop12": "junpufan@me.com",
# >>> "prop13": 0.1, "prop14": true}
