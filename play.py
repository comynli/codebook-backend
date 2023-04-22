from datetime import datetime
from gitea.api.repository_api import RepositoryApi
from gitea.configuration import Configuration
from gitea.api_client import ApiClient

if __name__ == '__main__':
    configuration = Configuration(
        host="https://git.mindcube.xyz/api/v1",
        api_key={"AuthorizationHeaderToken": "bb30e3a76dd8d4ef8b99638c3cc377f08d0121b5"},
        api_key_prefix={"AuthorizationHeaderToken": "token"}
    )
    # configuration.debug = True
    client = ApiClient(configuration)
    commits, status, headers = RepositoryApi(client).repo_get_all_commits("comyn", "notebox",
                                                                          page=1, limit=5,
                                                                          _check_return_type=False,
                                                                          _return_http_data_only=False)
    print(len(commits))
    print(headers.get("x-page"))
    print(headers.get("x-perpage"))
    print(headers.get("x-total"))
