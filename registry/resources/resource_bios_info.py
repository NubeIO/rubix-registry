from typing import Union

from tinydb import Query

from registry.models.model_bios_info import BiosInfoModel

bios_info_query = Query()


def put_bios_info(model: BiosInfoModel):
    with BiosInfoModel.get_db() as db:
        return db.upsert(model.to_dict(), bios_info_query.port.exists())


def get_bios_info() -> Union[BiosInfoModel, None]:
    with BiosInfoModel.get_db() as db:
        bios_info = db.search(bios_info_query.port.exists())
        return BiosInfoModel(**bios_info[0]) if bios_info else None


def get_bios_info_dict() -> dict:
    with BiosInfoModel.get_db() as db:
        bios_info = db.search(bios_info_query.port.exists())
        return bios_info[0] if bios_info else None
