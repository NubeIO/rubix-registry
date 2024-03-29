from typing import Union

from tinydb import Query

from registry.models.model_github_info import GitHubInfoModel

github_info_query = Query()


def put_github_info(model: GitHubInfoModel):
    with GitHubInfoModel.get_db() as db:
        return db.upsert(model.to_dict(), github_info_query.token.exists())


def get_github_info() -> Union[GitHubInfoModel, None]:
    with GitHubInfoModel.get_db() as db:
        github_info = db.search(github_info_query.token.exists())
        return GitHubInfoModel(**github_info[0]) if github_info else None


def get_github_info_dict() -> dict:
    with GitHubInfoModel.get_db() as db:
        github_info = db.search(github_info_query.token.exists())
        return github_info[0] if github_info else None
