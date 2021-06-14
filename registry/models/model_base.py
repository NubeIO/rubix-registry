import json
from abc import ABC


class ModelBase(ABC):

    def reload(self, setting: dict):
        if setting is not None:
            self.__dict__ = {k: setting.get(k, v) for k, v in self.__dict__.items()}
        return self

    def serialize(self, pretty=True) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=2 if pretty else None)

    def to_dict(self):
        return json.loads(self.serialize(pretty=False))
