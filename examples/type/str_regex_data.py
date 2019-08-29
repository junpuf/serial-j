from serial_j import SerialJ


class StrRegexData(SerialJ):
    schema = [
        {'name': 'prop1',
         'type': (str, r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")}
    ]


valid_data = StrRegexData({'prop1': 'anyone@emailservice.com'})
print(valid_data)
# >>> {"prop1": "anyone@emailservice.com"}

invalid_data = StrRegexData({'prop1': 'anyoneemailsea?rv@ice.com'})
# >>> ValueError: Property: 'prop1' with Value: 'anyoneemailsea?rv@ice.com' does not confirm with Type: (<class 'str'>, '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)').
