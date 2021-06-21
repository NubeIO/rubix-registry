from typing import Union

from tinydb import Query

from registry.models.model_github_info import GitHubInfoModel

github_info_query = Query()


def put_github_info(model: GitHubInfoModel):
    return GitHubInfoModel.get_db().upsert(model.to_dict(), github_info_query.token.exists())


def get_github_info() -> Union[GitHubInfoModel, None]:
    github_info = GitHubInfoModel.get_db().search(github_info_query.token.exists())
    return GitHubInfoModel(**github_info[0]) if github_info else None


def get_github_info_dict() -> dict:
    github_info = GitHubInfoModel.get_db().search(github_info_query.token.exists())
    return github_info[0] if github_info else None
