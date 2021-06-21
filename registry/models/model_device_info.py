from datetime import datetime

import shortuuid

from registry.models.model_base import ModelBase


class DeviceInfoModel(ModelBase):
    def __init__(self, **kwargs):
        self.global_uuid: str = kwargs.get("global_uuid", shortuuid.uuid())
        self.client_id: str = kwargs.get("client_id", "")
        self.client_name: str = kwargs.get("client_name", "")
        self.site_id: str = kwargs.get("site_id", "")
        self.site_name: str = kwargs.get("site_name", "")
        self.device_id: str = kwargs.get("device_id", shortuuid.uuid())
        self.device_name: str = kwargs.get("device_name", "")
        self.site_address: str = kwargs.get("site_address", "")
        self.site_city: str = kwargs.get("site_city", "")
        self.site_state: str = kwargs.get("site_state", "")
        self.site_zip: str = kwargs.get("site_zip", "")
        self.site_country: str = kwargs.get("site_country", "")
        self.site_lat: str = kwargs.get("site_lat", "")
        self.site_lon: str = kwargs.get("site_lon", "")
        self.time_zone: str = kwargs.get("time_zone", "Australia/Sydney")
        self.created_on: str = kwargs.get("created_on", datetime.utcnow().isoformat())
        self.updated_on: str = kwargs.get("updated_on", datetime.utcnow().isoformat())

    @classmethod
    def get_db_file(cls) -> str:
        return 'device_info.json'
