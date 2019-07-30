import re
import socket
import uuid

email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
url_regex = (f"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F]"
             f"[0-9a-fA-F]))+")

email_pattern = re.compile(email_regex)
url_pattern = re.compile(url_regex)


def _regex_match(regex, _str):
    try:
        pt = re.compile(regex)
        return pt.fullmatch(_str) is not None
    except re.error:
        return False


def _valid_regex(_str):
    try:
        re.compile(_str)
        return True
    except re.error:
        return False


def _valid_ipv4(_str):
    try:
        socket.inet_aton(_str)
        return True
    except:
        return False


def _valid_ipv6(_str):
    try:
        socket.inet_pton(socket.AF_INET6, _str)
        return True
    except:
        return False


def _valid_uuid(_str):
    if isinstance(_str, uuid.UUID):
        return True
    try:
        uuid.UUID(_str)
        return True
    except:
        return False


def _valid_email(_str):
    return email_pattern.fullmatch(_str) is not None


def _valid_url(_str):
    return url_pattern.fullmatch(_str) is not None


def _err(e, _name, _type=None, data=None):
    if e == 0:
        return f"Property '{_name}' not found in {data}."
    elif e == 1:
        return f"Property '{_name}' is not nullable."
    elif e == 2:
        return f"Compound Property '{_name}' is not of type list or dict."
    elif e == 3:
        return (f"Compound Property '{_name}' does not have a proper "
                f"serializer or schema.")
    elif e == 4:
        return (f"Property: '{_name}' with Value: '{data}' does not confirm "
                f"with Type: {str(_type)}.")
    elif e == 5:
        return f"Type: {str(_type)} for property '{_name}' is not valid."
