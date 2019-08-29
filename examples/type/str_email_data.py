from serial_j import SerialJ


class StrEmailData(SerialJ):
    schema = [
        {'name': 'prop1', 'type': (str, 'email')}
    ]


valid_data = StrEmailData({'prop1': 'anyone@emailservice.com'})
print(valid_data)
# >>> {"prop1": "anyone@emailservice.com"}
valid_data = StrEmailData({'prop1': 'any.one@emailservice.com'})
print(valid_data)
# >>> {"prop1": "any.one@emailservice.com"}

invalid_data = StrEmailData({'prop1': 'anyoneemailsea?rv@ice.com'})
# >>> ValueError: Property: 'prop1' with Value: 'anyoneemailsea?rv@ice.com' does not confirm with Type: (<class 'str'>, 'email').
