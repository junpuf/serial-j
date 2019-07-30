import json

from types import LambdaType

from serial_j.hp import _err, _valid_ipv4, _valid_ipv6, _valid_regex, \
    _valid_uuid, _valid_email, _valid_url, _regex_match, uuid

name = "serial_j"


class SerialJ(object):
    schema = []

    _na = 'name'
    _tp = 'type'
    _opt = 'optional'
    _nu = 'nullable'
    _cp = 'is_compound'
    _srl = 'compound_serializer'
    _sch = 'compound_schema'

    _spbtps = (int, float, bool, str)

    _empt = (None, "", (), [], {})

    _spsstps = dict(
        uuid=_valid_uuid,
        ipv4=_valid_ipv4,
        ipv6=_valid_ipv6,
        email=_valid_email,
        url=_valid_url
    )

    def __init__(self, data):
        self._preproc(data)
        self._proc(data)

    def _valid_type(self, _type):
        if isinstance(_type, tuple) and len(_type) == 2:
            mt = _type[0]
            st = _type[1]
            if mt not in self._spbtps:
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
                    and st not in self._spsstps.keys()
                    and not _valid_regex(st)):
                return False
            if mt == str and isinstance(st, tuple):
                for e in st:
                    if not isinstance(e, str):
                        return False
            return True
        elif isinstance(_type, tuple) and len(_type) == 1:
            mt = _type[0]
            if mt not in self._spbtps:
                return False
            return True
        else:
            return False

    def _validated(self, _type, data):
        if isinstance(_type, tuple) and len(_type) == 2:
            mt = _type[0]
            st = _type[1]
            if mt == int and (isinstance(st, tuple) or isinstance(st, range)):
                return data in st
            elif mt == int and isinstance(st, LambdaType):
                return st(data)
            elif mt == str and isinstance(st, tuple):
                return data in st
            elif mt == str and st in self._spsstps.keys():
                return self._spsstps[st](data)
            else:
                return _regex_match(regex=st, _str=data)
        elif isinstance(_type, tuple) and len(_type) == 1:
            mt = _type[0]
            return isinstance(data, mt)
        else:
            return False

    def _preproc(self, data):
        for prop in self.schema:
            _name = prop[self._na]
            _type = prop[self._tp] if self._tp in prop else None
            _optional = prop[self._opt] if self._opt in prop else False
            _nullable = prop[self._nu] if self._nu in prop else False
            _compound = prop[self._cp] if self._cp in prop else False
            _serializer = prop[self._srl] if self._srl in prop else None
            _schema = prop[self._sch] if self._sch in prop else None
            if _type and not self._valid_type(_type):
                raise TypeError(_err(5, _name, _type))
            if not _optional and _name not in data:
                raise ValueError(_err(0, _name, data))
            if _name in data:
                if not _nullable and data[_name] in self._empt:
                    raise ValueError(_err(1, _name))
                if _type and not self._validated(_type, data[_name]):
                    if _nullable and data[_name] == None:
                        pass
                    else:
                        raise ValueError(_err(4, _name, _type, data[_name]))
                if (_compound and not isinstance(data[_name], list)
                        and not isinstance(data[_name], dict)):
                    raise TypeError(_err(2, _name))
                if _compound and not _serializer and not _schema:
                    raise TypeError(_err(3, _name))
            prop[self._na] = _name
            prop[self._tp] = _type
            prop[self._opt] = _optional
            prop[self._nu] = _nullable
            prop[self._cp] = _compound
            prop[self._srl] = _serializer
            prop[self._sch] = _schema

    def _proc(self, data):
        for prop in self.schema:
            _name = prop[self._na]
            if _name in data:
                if prop[self._cp]:
                    if prop[self._srl]:
                        if isinstance(data[_name], list):
                            self.__dict__[_name] = [prop[self._srl](o)
                                                    for o in data[_name]]
                        elif isinstance(data[_name], dict):
                            self.__dict__[_name] = prop[self._srl](data[_name])
                    elif prop[self._sch]:
                        _cls = SerialJ
                        _cls.schema = prop[self._sch]
                        if isinstance(data[_name], list):
                            self.__dict__[_name] = [_cls(o)
                                                    for o in data[_name]]
                        elif isinstance(data[_name], dict):
                            self.__dict__[_name] = _cls(data[_name])
                else:
                    if isinstance(data[_name], uuid.UUID):
                        self.__dict__[_name] = str(data[_name])
                    else:
                        self.__dict__[_name] = data[_name]

    def as_dict(self):
        _d = {}
        for prop in self.schema:
            _name = prop[self._na]
            if prop[self._cp]:
                if isinstance(self.__dict__[_name], list):
                    _d[_name] = [cp.as_dict() for cp in self.__dict__[_name]]
                else:
                    _d[_name] = self.__dict__[_name].as_dict()
            else:
                if _name in self.__dict__:
                    _d[_name] = self.__dict__[_name]
        return _d

    def _to_str(self):
        return json.dumps(self.as_dict())

    def __str__(self) -> str:
        return self._to_str()

    def __repr__(self) -> str:
        return self._to_str()
