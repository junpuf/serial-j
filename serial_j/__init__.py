import json
from types import LambdaType
from uuid import UUID
from serial_j.hp import _valid_regex, _regex_match, _err, _spsstps
from serial_j.const import _spbtps, _na, _nu, _tp, _opt, _cp, _srl, \
    _sch, _empt

name = "serial_j"


class SerialJ(object):
    schema = []

    def __init__(self, data):
        self._preproc(data)
        self._proc(data)

    @staticmethod
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

    @staticmethod
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

    def _preproc(self, data):
        for prop in self.schema:
            _name = prop[_na]
            _type = prop[_tp] if _tp in prop else None
            _optional = prop[_opt] if _opt in prop else False
            _nullable = prop[_nu] if _nu in prop else False
            _compound = prop[_cp] if _cp in prop else False
            _serializer = prop[_srl] if _srl in prop else None
            _schema = prop[_sch] if _sch in prop else None
            if _type and not self._valid_type(_type):
                raise TypeError(_err(5, _name, _type))
            if not _optional and _name not in data:
                raise ValueError(_err(0, _name, data))
            if _name in data:
                if data[_name] in _empt:
                    if not _nullable:
                        raise ValueError(_err(1, _name))
                else:
                    if _type and not self._validated(_type, data[_name]):
                        raise ValueError(_err(4, _name, _type, data[_name]))
                    if (_compound and not isinstance(data[_name], list)
                            and not isinstance(data[_name], dict)):
                        raise TypeError(_err(2, _name))
                    if _compound and not _serializer and not _schema:
                        raise TypeError(_err(3, _name))
            prop[_na] = _name
            prop[_tp] = _type
            prop[_opt] = _optional
            prop[_nu] = _nullable
            prop[_cp] = _compound
            prop[_srl] = _serializer
            prop[_sch] = _schema

    def _proc(self, data):
        for prop in self.schema:
            _name = prop[_na]
            if _name in data:
                if prop[_cp]:
                    if prop[_srl]:
                        if isinstance(data[_name], list):
                            self.__dict__[_name] = [prop[_srl](o)
                                                    for o in data[_name]]
                        elif isinstance(data[_name], dict):
                            self.__dict__[_name] = prop[_srl](data[_name])
                    elif prop[_sch]:
                        _cls = SerialJ
                        _cls.schema = prop[_sch]
                        if isinstance(data[_name], list):
                            self.__dict__[_name] = [_cls(o)
                                                    for o in data[_name]]
                        elif isinstance(data[_name], dict):
                            self.__dict__[_name] = _cls(data[_name])
                else:
                    if isinstance(data[_name], UUID):
                        self.__dict__[_name] = str(data[_name])
                    else:
                        self.__dict__[_name] = data[_name]

    def as_dict(self):
        _d = {}
        for prop in self.schema:
            _name = prop[_na]
            if prop[_cp]:
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
