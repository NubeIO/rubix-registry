from typing import Union

from tinydb import Query

from registry.models.model_device_info import DeviceInfoModel

device_info_query = Query()


def put_device_info(model: DeviceInfoModel):
    with DeviceInfoModel.get_db() as db:
        return db.upsert(model.to_dict(), device_info_query.global_uuid.exists())


def get_device_info() -> Union[DeviceInfoModel, None]:
    with DeviceInfoModel.get_db() as db:
        device_info = db.search(device_info_query.global_uuid.exists())
        return DeviceInfoModel(**device_info[0]) if device_info else None


def get_device_info_dict() -> dict:
    with DeviceInfoModel.get_db() as db:
        device_info = db.search(device_info_query.global_uuid.exists())
        return device_info[0] if device_info else None
