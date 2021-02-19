import json
import logging
import os

from registry.utils.file import write_file, read_file
from registry.utils.singleton import Singleton

logger = logging.getLogger(__name__)


class RubixRegistry(metaclass=Singleton):
    out: str = '/data/rubix-registry'
    default_wires_plat_file: str = 'wires-plat.json'

    def __init__(self, data_dir: str = None):
        self.__data_dir = self.__compute_dir(data_dir or RubixRegistry.out)
        self.__wires_plat_file = os.path.join(self.data_dir, self.default_wires_plat_file)

    @property
    def data_dir(self):
        return self.__data_dir

    @property
    def wires_plat_file(self):
        return self.__wires_plat_file

    @staticmethod
    def __compute_dir(_dir: str, mode=0o744) -> str:
        d = _dir if os.path.isabs(_dir) else os.path.join(os.getcwd(), _dir)
        os.makedirs(d, mode, True)
        return d

    def store_wires_plat(self, data: dict) -> dict:
        write_file(self.wires_plat_file, json.dumps(data))
        return data

    def read_wires_plat(self) -> dict:
        # we optimize this one if needed
        try:
            data: str = read_file(self.wires_plat_file)
            return json.loads(data)
        except Exception as e:
            logger.error(str(e))
            return {}

    def delete_wires_plat(self):
        os.remove(self.wires_plat_file)
