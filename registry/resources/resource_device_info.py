import os
from typing import Union

from tinydb import TinyDB, Query

from registry.constants import RUBIX_REGISTRY_DIR
from registry.models.model_device_info import DeviceInfoModel

db = TinyDB(os.path.join(RUBIX_REGISTRY_DIR, 'device_info.json'))
device_info_query = Query()


def put_device_info(model: DeviceInfoModel):
    return db.upsert(model.to_dict(), device_info_query.global_uuid.exists())


def get_device_info() -> Union[DeviceInfoModel, None]:
    device_info = db.search(device_info_query.global_uuid.exists())
    return DeviceInfoModel(**device_info[0]) if device_info else None


def get_device_info_dict() -> dict:
    device_info = db.search(device_info_query.global_uuid.exists())
    return device_info[0] if device_info else None
