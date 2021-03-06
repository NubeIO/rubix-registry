from registry.models.model_base import ModelBase


class BiosInfoModel(ModelBase):
    def __init__(self, **kwargs):
        self.port: int = kwargs.get("port", 1615)

    @classmethod
    def get_db_file(cls) -> str:
        return 'rubix_bios_info.json'
