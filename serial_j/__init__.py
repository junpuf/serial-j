import json
from uuid import UUID

from serial_j.const import _spbtps, _na, _nu, _tp, _opt, _cp, _srl, \
    _sch, _empt, _spopts
from serial_j.hp import _err, _spsstps, _valid_type, _valid_regex, _validated

name = "serial_j"


def create_schema(schema=None):
    def validate_schema(schema):
        if schema is None or not isinstance(schema, list):
            raise TypeError(_err(7))
        else:
            for p in schema:
                if not isinstance(p, dict):
                    raise TypeError(_err(8))
                elif _na not in p.keys():
                    raise TypeError(_err(12))
                else:
                    keys = p.keys()
                    name = p.get(_na)
                    for opt in keys:
                        if opt not in _spopts:
                            raise TypeError(_err(9, opt))
                        elif opt == _tp and not _valid_type(p.get(_tp)):
                            raise TypeError(_err(10, p.get(_tp)))
                        elif opt == _cp and p.get(_cp):
                            if not _srl in keys and not _sch in keys:
                                raise TypeError(_err(11))
                            elif _srl in keys and _sch in keys:
                                raise TypeError(_err(13))
                            elif _srl in keys:
                                validate_schema(p.get(_srl).schema)
                            elif _sch in keys:
                                validate_schema(p.get(_sch))
                        elif opt == _opt and not isinstance(p.get(_opt), bool):
                            raise TypeError(
                                _err(14, _name=name, opt=_opt, _type=bool))
                        elif opt == _nu and not isinstance(p.get(_nu), bool):
                            raise TypeError(
                                _err(14, _name=name, opt=_nu, _type=bool))

    validate_schema(schema)
    return schema


class SerialJ(object):
    schema = []

    def __init__(self, data):
        self._preproc(data)
        self._proc(data)

    def _preproc(self, data):
        for prop in self.schema:
            _name = prop[_na]
            _type = prop[_tp] if _tp in prop else None
            _optional = prop[_opt] if _opt in prop else False
            _nullable = prop[_nu] if _nu in prop else False
            _compound = prop[_cp] if _cp in prop else False
            _serializer = prop[_srl] if _srl in prop else None
            _schema = prop[_sch] if _sch in prop else None
            if _type and not _valid_type(_type):
                raise TypeError(_err(5, _name, _type))
            if not _optional and _name not in data:
                raise ValueError(_err(0, _name, data))
            if _name in data:
                if data[_name] in _empt:
                    if not _nullable:
                        raise ValueError(_err(1, _name))
                else:
                    if _type and not _validated(_type, data[_name]):
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
