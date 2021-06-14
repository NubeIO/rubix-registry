from registry.models.model_base import ModelBase


class GitHubInfoModel(ModelBase):
    def __init__(self, **kwargs):
        self.token: str = kwargs.get("token", "")
