import re
import socket
import uuid
from types import LambdaType

from serial_j.const import _spbtps

email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
url_regex = (
    f"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F]"
    f"[0-9a-fA-F]))+")
email_pattern = re.compile(email_regex)
url_pattern = re.compile(url_regex)


def _valid_email(_str):
    return email_pattern.fullmatch(_str) is not None


def _valid_url(_str):
    return url_pattern.fullmatch(_str) is not None


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


_spsstps = dict(
    uuid=_valid_uuid,
    ipv4=_valid_ipv4,
    ipv6=_valid_ipv6,
    email=_valid_email,
    url=_valid_url
)


def _valid_type(_type):
    if isinstance(_type, tuple) and len(_type) == 2:
        mt = _type[0]
        st = _type[1]
        if mt not in _spbtps:
            return False
        if (mt == int and not isinstance(st, tuple)
                and not isinstance(st, range)
                and not isinstance(st, LambdaType)):
            return False
        if mt == int and isinstance(st, tuple):
            for e in st:
                if not isinstance(e, int):
                    return False
        if (mt == str and not isinstance(st, tuple)
                and st not in _spsstps.keys()
                and not _valid_regex(st)):
            return False
        if mt == str and isinstance(st, tuple):
            for e in st:
                if not isinstance(e, str):
                    return False
        return True
    elif isinstance(_type, tuple) and len(_type) == 1:
        mt = _type[0]
        if mt not in _spbtps:
            return False
        return True
    else:
        return False


def _validated(_type, data):
    if isinstance(_type, tuple) and len(_type) == 2:
        mt = _type[0]
        st = _type[1]
        if mt == int and (isinstance(st, tuple) or isinstance(st, range)):
            return data in st
        elif mt == int and isinstance(st, LambdaType):
            return st(data)
        elif mt == str and isinstance(st, tuple):
            return data in st
        elif mt == str and st in _spsstps.keys():
            return _spsstps[st](data)
        else:
            return _regex_match(regex=st, _str=data)
    elif isinstance(_type, tuple) and len(_type) == 1:
        mt = _type[0]
        return isinstance(data, mt)
    else:
        return False


def _err(e, _name=None, _type=None, data=None, opt=None):
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
    elif e == 6:
        return f"Schema invalid, {opt} is not a valid option."
    elif e == 7:
        return f"Schema invalid, schema must be a list."
    elif e == 8:
        return f"Schema invalid, all property definitions must be a dict."
    elif e == 9:
        return f"Schema invalid, {opt} is not a valid option."
    elif e == 10:
        return f"Type: {str(_type)} is not valid."
    elif e == 11:
        return (f"Either `compound_serializer` or `compound_schema` "
                f"should be provided when `is_compound` was set to `True`.")
    elif e == 12:
        return "`name` is require to define a property."
    elif e == 13:
        return (f"You should not be providing both `compound_serializer` "
                f"and `compound_schema`.")
    elif e == 14:
        return (f"option: `{opt}` should be of type {_type}")
