from typing import Union

from tinydb import Query

from registry.models.model_device_info import DeviceInfoModel

device_info_query = Query()


def put_device_info(model: DeviceInfoModel):
    return DeviceInfoModel.get_db().upsert(model.to_dict(), device_info_query.global_uuid.exists())


def get_device_info() -> Union[DeviceInfoModel, None]:
    device_info = DeviceInfoModel.get_db().search(device_info_query.global_uuid.exists())
    return DeviceInfoModel(**device_info[0]) if device_info else None


def get_device_info_dict() -> dict:
    device_info = DeviceInfoModel.get_db().search(device_info_query.global_uuid.exists())
    return device_info[0] if device_info else None
