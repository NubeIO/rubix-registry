import os
from typing import Union

from tinydb import TinyDB, Query

from registry.constants import RUBIX_REGISTRY_DIR
from registry.models.model_github_info import GitHubInfoModel

db = TinyDB(os.path.join(RUBIX_REGISTRY_DIR, 'github_info.json'))
github_info_query = Query()


def put_github_info(model: GitHubInfoModel):
    return db.upsert(model.to_dict(), github_info_query.token.exists())


def get_github_info() -> Union[GitHubInfoModel, None]:
    github_info = db.search(github_info_query.token.exists())
    return GitHubInfoModel(**github_info[0]) if github_info else None


def get_github_info_dict() -> dict:
    github_info = db.search(github_info_query.token.exists())
    return github_info[0] if github_info else None
