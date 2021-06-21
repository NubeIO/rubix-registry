from typing import Union

from tinydb import Query

from registry.models.model_bios_info import BiosInfoModel

bios_info_query = Query()


def put_bios_info(model: BiosInfoModel):
    return BiosInfoModel.get_db().upsert(model.to_dict(), bios_info_query.port.exists())


def get_bios_info() -> Union[BiosInfoModel, None]:
    bios_info = BiosInfoModel.get_db().search(bios_info_query.port.exists())
    return BiosInfoModel(**bios_info[0]) if bios_info else None


def get_bios_info_dict() -> dict:
    bios_info = BiosInfoModel.get_db().search(bios_info_query.port.exists())
    return bios_info[0] if bios_info else None
