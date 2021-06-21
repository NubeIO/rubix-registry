import json
import os
from abc import ABC, abstractmethod

from tinydb import TinyDB

from registry.constants import RUBIX_REGISTRY_DIR


class ModelBase(ABC):

    def reload(self, setting: dict):
        if setting is not None:
            self.__dict__ = {k: setting.get(k, v) for k, v in self.__dict__.items()}
        return self

    def serialize(self, pretty=True) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=2 if pretty else None)

    def to_dict(self):
        return json.loads(self.serialize(pretty=False))

    @classmethod
    def get_db(cls) -> TinyDB:
        return TinyDB(os.path.join(RUBIX_REGISTRY_DIR, cls.get_db_file()))

    @classmethod
    @abstractmethod
    def get_db_file(cls) -> str:
        pass
