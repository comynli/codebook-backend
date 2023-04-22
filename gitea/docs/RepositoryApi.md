# gitea.RepositoryApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_current_user_repo**](RepositoryApi.md#create_current_user_repo) | **POST** /user/repos | Create a repository
[**create_fork**](RepositoryApi.md#create_fork) | **POST** /repos/{owner}/{repo}/forks | Fork a repository
[**get_blob**](RepositoryApi.md#get_blob) | **GET** /repos/{owner}/{repo}/git/blobs/{sha} | Gets the blob of a repository.
[**get_tag**](RepositoryApi.md#get_tag) | **GET** /repos/{owner}/{repo}/git/tags/{sha} | Gets the tag object of an annotated tag (not lightweight tags)
[**get_tree**](RepositoryApi.md#get_tree) | **GET** /repos/{owner}/{repo}/git/trees/{sha} | Gets the tree of a repository.
[**list_forks**](RepositoryApi.md#list_forks) | **GET** /repos/{owner}/{repo}/forks | List a repository&#39;s forks
[**repo_add_collaborator**](RepositoryApi.md#repo_add_collaborator) | **PUT** /repos/{owner}/{repo}/collaborators/{collaborator} | Add a collaborator to a repository
[**repo_add_team**](RepositoryApi.md#repo_add_team) | **PUT** /repos/{owner}/{repo}/teams/{team} | Add a team to a repository
[**repo_add_topc**](RepositoryApi.md#repo_add_topc) | **PUT** /repos/{owner}/{repo}/topics/{topic} | Add a topic to a repository
[**repo_check_collaborator**](RepositoryApi.md#repo_check_collaborator) | **GET** /repos/{owner}/{repo}/collaborators/{collaborator} | Check if a user is a collaborator of a repository
[**repo_check_team**](RepositoryApi.md#repo_check_team) | **GET** /repos/{owner}/{repo}/teams/{team} | Check if a team is assigned to a repository
[**repo_create_branch**](RepositoryApi.md#repo_create_branch) | **POST** /repos/{owner}/{repo}/branches | Create a branch
[**repo_create_branch_protection**](RepositoryApi.md#repo_create_branch_protection) | **POST** /repos/{owner}/{repo}/branch_protections | Create a branch protections for a repository
[**repo_create_file**](RepositoryApi.md#repo_create_file) | **POST** /repos/{owner}/{repo}/contents/{filepath} | Create a file in a repository
[**repo_create_hook**](RepositoryApi.md#repo_create_hook) | **POST** /repos/{owner}/{repo}/hooks | Create a hook
[**repo_create_key**](RepositoryApi.md#repo_create_key) | **POST** /repos/{owner}/{repo}/keys | Add a key to a repository
[**repo_create_pull_request**](RepositoryApi.md#repo_create_pull_request) | **POST** /repos/{owner}/{repo}/pulls | Create a pull request
[**repo_create_pull_review**](RepositoryApi.md#repo_create_pull_review) | **POST** /repos/{owner}/{repo}/pulls/{index}/reviews | Create a review to an pull request
[**repo_create_pull_review_requests**](RepositoryApi.md#repo_create_pull_review_requests) | **POST** /repos/{owner}/{repo}/pulls/{index}/requested_reviewers | create review requests for a pull request
[**repo_create_release**](RepositoryApi.md#repo_create_release) | **POST** /repos/{owner}/{repo}/releases | Create a release
[**repo_create_release_attachment**](RepositoryApi.md#repo_create_release_attachment) | **POST** /repos/{owner}/{repo}/releases/{id}/assets | Create a release attachment
[**repo_create_status**](RepositoryApi.md#repo_create_status) | **POST** /repos/{owner}/{repo}/statuses/{sha} | Create a commit status
[**repo_delete**](RepositoryApi.md#repo_delete) | **DELETE** /repos/{owner}/{repo} | Delete a repository
[**repo_delete_branch**](RepositoryApi.md#repo_delete_branch) | **DELETE** /repos/{owner}/{repo}/branches/{branch} | Delete a specific branch from a repository
[**repo_delete_branch_protection**](RepositoryApi.md#repo_delete_branch_protection) | **DELETE** /repos/{owner}/{repo}/branch_protections/{name} | Delete a specific branch protection for the repository
[**repo_delete_collaborator**](RepositoryApi.md#repo_delete_collaborator) | **DELETE** /repos/{owner}/{repo}/collaborators/{collaborator} | Delete a collaborator from a repository
[**repo_delete_file**](RepositoryApi.md#repo_delete_file) | **DELETE** /repos/{owner}/{repo}/contents/{filepath} | Delete a file in a repository
[**repo_delete_git_hook**](RepositoryApi.md#repo_delete_git_hook) | **DELETE** /repos/{owner}/{repo}/hooks/git/{id} | Delete a Git hook in a repository
[**repo_delete_hook**](RepositoryApi.md#repo_delete_hook) | **DELETE** /repos/{owner}/{repo}/hooks/{id} | Delete a hook in a repository
[**repo_delete_key**](RepositoryApi.md#repo_delete_key) | **DELETE** /repos/{owner}/{repo}/keys/{id} | Delete a key from a repository
[**repo_delete_pull_review**](RepositoryApi.md#repo_delete_pull_review) | **DELETE** /repos/{owner}/{repo}/pulls/{index}/reviews/{id} | Delete a specific review from a pull request
[**repo_delete_pull_review_requests**](RepositoryApi.md#repo_delete_pull_review_requests) | **DELETE** /repos/{owner}/{repo}/pulls/{index}/requested_reviewers | cancel review requests for a pull request
[**repo_delete_release**](RepositoryApi.md#repo_delete_release) | **DELETE** /repos/{owner}/{repo}/releases/{id} | Delete a release
[**repo_delete_release_attachment**](RepositoryApi.md#repo_delete_release_attachment) | **DELETE** /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | Delete a release attachment
[**repo_delete_release_by_tag**](RepositoryApi.md#repo_delete_release_by_tag) | **DELETE** /repos/{owner}/{repo}/releases/tags/{tag} | Delete a release by tag name
[**repo_delete_tag**](RepositoryApi.md#repo_delete_tag) | **DELETE** /repos/{owner}/{repo}/tags/{tag} | Delete a repository&#39;s tag by name
[**repo_delete_team**](RepositoryApi.md#repo_delete_team) | **DELETE** /repos/{owner}/{repo}/teams/{team} | Delete a team from a repository
[**repo_delete_topic**](RepositoryApi.md#repo_delete_topic) | **DELETE** /repos/{owner}/{repo}/topics/{topic} | Delete a topic from a repository
[**repo_dismiss_pull_review**](RepositoryApi.md#repo_dismiss_pull_review) | **POST** /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals | Dismiss a review for a pull request
[**repo_download_pull_diff**](RepositoryApi.md#repo_download_pull_diff) | **GET** /repos/{owner}/{repo}/pulls/{index}.diff | Get a pull request diff
[**repo_download_pull_patch**](RepositoryApi.md#repo_download_pull_patch) | **GET** /repos/{owner}/{repo}/pulls/{index}.patch | Get a pull request patch file
[**repo_edit**](RepositoryApi.md#repo_edit) | **PATCH** /repos/{owner}/{repo} | Edit a repository&#39;s properties. Only fields that are set will be changed.
[**repo_edit_branch_protection**](RepositoryApi.md#repo_edit_branch_protection) | **PATCH** /repos/{owner}/{repo}/branch_protections/{name} | Edit a branch protections for a repository. Only fields that are set will be changed
[**repo_edit_git_hook**](RepositoryApi.md#repo_edit_git_hook) | **PATCH** /repos/{owner}/{repo}/hooks/git/{id} | Edit a Git hook in a repository
[**repo_edit_hook**](RepositoryApi.md#repo_edit_hook) | **PATCH** /repos/{owner}/{repo}/hooks/{id} | Edit a hook in a repository
[**repo_edit_pull_request**](RepositoryApi.md#repo_edit_pull_request) | **PATCH** /repos/{owner}/{repo}/pulls/{index} | Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.
[**repo_edit_release**](RepositoryApi.md#repo_edit_release) | **PATCH** /repos/{owner}/{repo}/releases/{id} | Update a release
[**repo_edit_release_attachment**](RepositoryApi.md#repo_edit_release_attachment) | **PATCH** /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | Edit a release attachment
[**repo_get**](RepositoryApi.md#repo_get) | **GET** /repos/{owner}/{repo} | Get a repository
[**repo_get_all_commits**](RepositoryApi.md#repo_get_all_commits) | **GET** /repos/{owner}/{repo}/commits | Get a list of all commits from a repository
[**repo_get_archive**](RepositoryApi.md#repo_get_archive) | **GET** /repos/{owner}/{repo}/archive/{archive} | Get an archive of a repository
[**repo_get_branch**](RepositoryApi.md#repo_get_branch) | **GET** /repos/{owner}/{repo}/branches/{branch} | Retrieve a specific branch from a repository, including its effective branch protection
[**repo_get_branch_protection**](RepositoryApi.md#repo_get_branch_protection) | **GET** /repos/{owner}/{repo}/branch_protections/{name} | Get a specific branch protection for the repository
[**repo_get_by_id**](RepositoryApi.md#repo_get_by_id) | **GET** /repositories/{id} | Get a repository by id
[**repo_get_combined_status_by_ref**](RepositoryApi.md#repo_get_combined_status_by_ref) | **GET** /repos/{owner}/{repo}/commits/{ref}/status | Get a commit&#39;s combined status, by branch/tag/commit reference
[**repo_get_contents**](RepositoryApi.md#repo_get_contents) | **GET** /repos/{owner}/{repo}/contents/{filepath} | Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir
[**repo_get_contents_list**](RepositoryApi.md#repo_get_contents_list) | **GET** /repos/{owner}/{repo}/contents | Gets the metadata of all the entries of the root dir
[**repo_get_editor_config**](RepositoryApi.md#repo_get_editor_config) | **GET** /repos/{owner}/{repo}/editorconfig/{filepath} | Get the EditorConfig definitions of a file in a repository
[**repo_get_git_hook**](RepositoryApi.md#repo_get_git_hook) | **GET** /repos/{owner}/{repo}/hooks/git/{id} | Get a Git hook
[**repo_get_hook**](RepositoryApi.md#repo_get_hook) | **GET** /repos/{owner}/{repo}/hooks/{id} | Get a hook
[**repo_get_issue_templates**](RepositoryApi.md#repo_get_issue_templates) | **GET** /repos/{owner}/{repo}/issue_templates | Get available issue templates for a repository
[**repo_get_key**](RepositoryApi.md#repo_get_key) | **GET** /repos/{owner}/{repo}/keys/{id} | Get a repository&#39;s key by id
[**repo_get_languages**](RepositoryApi.md#repo_get_languages) | **GET** /repos/{owner}/{repo}/languages | Get languages and number of bytes of code written
[**repo_get_pull_request**](RepositoryApi.md#repo_get_pull_request) | **GET** /repos/{owner}/{repo}/pulls/{index} | Get a pull request
[**repo_get_pull_review**](RepositoryApi.md#repo_get_pull_review) | **GET** /repos/{owner}/{repo}/pulls/{index}/reviews/{id} | Get a specific review for a pull request
[**repo_get_pull_review_comments**](RepositoryApi.md#repo_get_pull_review_comments) | **GET** /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments | Get a specific review for a pull request
[**repo_get_raw_file**](RepositoryApi.md#repo_get_raw_file) | **GET** /repos/{owner}/{repo}/raw/{filepath} | Get a file from a repository
[**repo_get_release**](RepositoryApi.md#repo_get_release) | **GET** /repos/{owner}/{repo}/releases/{id} | Get a release
[**repo_get_release_attachment**](RepositoryApi.md#repo_get_release_attachment) | **GET** /repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | Get a release attachment
[**repo_get_release_by_tag**](RepositoryApi.md#repo_get_release_by_tag) | **GET** /repos/{owner}/{repo}/releases/tags/{tag} | Get a release by tag name
[**repo_get_single_commit**](RepositoryApi.md#repo_get_single_commit) | **GET** /repos/{owner}/{repo}/git/commits/{sha} | Get a single commit from a repository
[**repo_list_all_git_refs**](RepositoryApi.md#repo_list_all_git_refs) | **GET** /repos/{owner}/{repo}/git/refs | Get specified ref or filtered repository&#39;s refs
[**repo_list_branch_protection**](RepositoryApi.md#repo_list_branch_protection) | **GET** /repos/{owner}/{repo}/branch_protections | List branch protections for a repository
[**repo_list_branches**](RepositoryApi.md#repo_list_branches) | **GET** /repos/{owner}/{repo}/branches | List a repository&#39;s branches
[**repo_list_collaborators**](RepositoryApi.md#repo_list_collaborators) | **GET** /repos/{owner}/{repo}/collaborators | List a repository&#39;s collaborators
[**repo_list_git_hooks**](RepositoryApi.md#repo_list_git_hooks) | **GET** /repos/{owner}/{repo}/hooks/git | List the Git hooks in a repository
[**repo_list_git_refs**](RepositoryApi.md#repo_list_git_refs) | **GET** /repos/{owner}/{repo}/git/refs/{ref} | Get specified ref or filtered repository&#39;s refs
[**repo_list_hooks**](RepositoryApi.md#repo_list_hooks) | **GET** /repos/{owner}/{repo}/hooks | List the hooks in a repository
[**repo_list_keys**](RepositoryApi.md#repo_list_keys) | **GET** /repos/{owner}/{repo}/keys | List a repository&#39;s keys
[**repo_list_pull_requests**](RepositoryApi.md#repo_list_pull_requests) | **GET** /repos/{owner}/{repo}/pulls | List a repo&#39;s pull requests
[**repo_list_pull_reviews**](RepositoryApi.md#repo_list_pull_reviews) | **GET** /repos/{owner}/{repo}/pulls/{index}/reviews | List all reviews for a pull request
[**repo_list_release_attachments**](RepositoryApi.md#repo_list_release_attachments) | **GET** /repos/{owner}/{repo}/releases/{id}/assets | List release&#39;s attachments
[**repo_list_releases**](RepositoryApi.md#repo_list_releases) | **GET** /repos/{owner}/{repo}/releases | List a repo&#39;s releases
[**repo_list_stargazers**](RepositoryApi.md#repo_list_stargazers) | **GET** /repos/{owner}/{repo}/stargazers | List a repo&#39;s stargazers
[**repo_list_statuses**](RepositoryApi.md#repo_list_statuses) | **GET** /repos/{owner}/{repo}/statuses/{sha} | Get a commit&#39;s statuses
[**repo_list_statuses_by_ref**](RepositoryApi.md#repo_list_statuses_by_ref) | **GET** /repos/{owner}/{repo}/commits/{ref}/statuses | Get a commit&#39;s statuses, by branch/tag/commit reference
[**repo_list_subscribers**](RepositoryApi.md#repo_list_subscribers) | **GET** /repos/{owner}/{repo}/subscribers | List a repo&#39;s watchers
[**repo_list_tags**](RepositoryApi.md#repo_list_tags) | **GET** /repos/{owner}/{repo}/tags | List a repository&#39;s tags
[**repo_list_teams**](RepositoryApi.md#repo_list_teams) | **GET** /repos/{owner}/{repo}/teams | List a repository&#39;s teams
[**repo_list_topics**](RepositoryApi.md#repo_list_topics) | **GET** /repos/{owner}/{repo}/topics | Get list of topics that a repository has
[**repo_merge_pull_request**](RepositoryApi.md#repo_merge_pull_request) | **POST** /repos/{owner}/{repo}/pulls/{index}/merge | Merge a pull request
[**repo_migrate**](RepositoryApi.md#repo_migrate) | **POST** /repos/migrate | Migrate a remote git repository
[**repo_mirror_sync**](RepositoryApi.md#repo_mirror_sync) | **POST** /repos/{owner}/{repo}/mirror-sync | Sync a mirrored repository
[**repo_pull_request_is_merged**](RepositoryApi.md#repo_pull_request_is_merged) | **GET** /repos/{owner}/{repo}/pulls/{index}/merge | Check if a pull request has been merged
[**repo_search**](RepositoryApi.md#repo_search) | **GET** /repos/search | Search for repositories
[**repo_signing_key**](RepositoryApi.md#repo_signing_key) | **GET** /repos/{owner}/{repo}/signing-key.gpg | Get signing-key.gpg for given repository
[**repo_submit_pull_review**](RepositoryApi.md#repo_submit_pull_review) | **POST** /repos/{owner}/{repo}/pulls/{index}/reviews/{id} | Submit a pending review to an pull request
[**repo_test_hook**](RepositoryApi.md#repo_test_hook) | **POST** /repos/{owner}/{repo}/hooks/{id}/tests | Test a push webhook
[**repo_tracked_times**](RepositoryApi.md#repo_tracked_times) | **GET** /repos/{owner}/{repo}/times | List a repo&#39;s tracked times
[**repo_transfer**](RepositoryApi.md#repo_transfer) | **POST** /repos/{owner}/{repo}/transfer | Transfer a repo ownership
[**repo_un_dismiss_pull_review**](RepositoryApi.md#repo_un_dismiss_pull_review) | **POST** /repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals | Cancel to dismiss a review for a pull request
[**repo_update_file**](RepositoryApi.md#repo_update_file) | **PUT** /repos/{owner}/{repo}/contents/{filepath} | Update a file in a repository
[**repo_update_pull_request**](RepositoryApi.md#repo_update_pull_request) | **POST** /repos/{owner}/{repo}/pulls/{index}/update | Merge PR&#39;s baseBranch into headBranch
[**repo_update_topics**](RepositoryApi.md#repo_update_topics) | **PUT** /repos/{owner}/{repo}/topics | Replace list of topics for a repository
[**topic_search**](RepositoryApi.md#topic_search) | **GET** /topics/search | search topics via keyword
[**user_current_check_subscription**](RepositoryApi.md#user_current_check_subscription) | **GET** /repos/{owner}/{repo}/subscription | Check if the current user is watching a repo
[**user_current_delete_subscription**](RepositoryApi.md#user_current_delete_subscription) | **DELETE** /repos/{owner}/{repo}/subscription | Unwatch a repo
[**user_current_put_subscription**](RepositoryApi.md#user_current_put_subscription) | **PUT** /repos/{owner}/{repo}/subscription | Watch a repo
[**user_tracked_times**](RepositoryApi.md#user_tracked_times) | **GET** /repos/{owner}/{repo}/times/{user} | List a user&#39;s tracked times in a repo


# **create_current_user_repo**
> Repository create_current_user_repo()

Create a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.repository import Repository
from gitea.model.create_repo_option import CreateRepoOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    body = CreateRepoOption(
        auto_init=True,
        default_branch="default_branch_example",
        description="description_example",
        gitignores="gitignores_example",
        issue_labels="issue_labels_example",
        license="license_example",
        name="name_example",
        private=True,
        readme="readme_example",
        template=True,
        trust_model="default",
    ) # CreateRepoOption |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a repository
        api_response = api_instance.create_current_user_repo(body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->create_current_user_repo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRepoOption**](CreateRepoOption.md)|  | [optional]

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Repository |  -  |
**409** | The repository with the same name already exists. |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fork**
> Repository create_fork(owner, repo)

Fork a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.create_fork_option import CreateForkOption
from gitea.model.repository import Repository
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo to fork
    repo = "repo_example" # str | name of the repo to fork
    body = CreateForkOption(
        organization="organization_example",
    ) # CreateForkOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fork a repository
        api_response = api_instance.create_fork(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->create_fork: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fork a repository
        api_response = api_instance.create_fork(owner, repo, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->create_fork: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to fork |
 **repo** | **str**| name of the repo to fork |
 **body** | [**CreateForkOption**](CreateForkOption.md)|  | [optional]

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Repository |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blob**
> GitBlobResponse get_blob(owner, repo, sha)

Gets the blob of a repository.

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.git_blob_response import GitBlobResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    sha = "sha_example" # str | sha of the commit

    # example passing only required values which don't have defaults set
    try:
        # Gets the blob of a repository.
        api_response = api_instance.get_blob(owner, repo, sha)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->get_blob: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **sha** | **str**| sha of the commit |

### Return type

[**GitBlobResponse**](GitBlobResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GitBlobResponse |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag**
> AnnotatedTag get_tag(owner, repo, sha)

Gets the tag object of an annotated tag (not lightweight tags)

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.annotated_tag import AnnotatedTag
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    sha = "sha_example" # str | sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags.

    # example passing only required values which don't have defaults set
    try:
        # Gets the tag object of an annotated tag (not lightweight tags)
        api_response = api_instance.get_tag(owner, repo, sha)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->get_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **sha** | **str**| sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags. |

### Return type

[**AnnotatedTag**](AnnotatedTag.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AnnotatedTag |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tree**
> GitTreeResponse get_tree(owner, repo, sha)

Gets the tree of a repository.

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.git_tree_response import GitTreeResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    sha = "sha_example" # str | sha of the commit
    recursive = True # bool | show all directories and files (optional)
    page = 1 # int | page number; the 'truncated' field in the response will be true if there are still more items after this page, false if the last page (optional)
    per_page = 1 # int | number of items per page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the tree of a repository.
        api_response = api_instance.get_tree(owner, repo, sha)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->get_tree: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the tree of a repository.
        api_response = api_instance.get_tree(owner, repo, sha, recursive=recursive, page=page, per_page=per_page)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->get_tree: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **sha** | **str**| sha of the commit |
 **recursive** | **bool**| show all directories and files | [optional]
 **page** | **int**| page number; the &#39;truncated&#39; field in the response will be true if there are still more items after this page, false if the last page | [optional]
 **per_page** | **int**| number of items per page | [optional]

### Return type

[**GitTreeResponse**](GitTreeResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GitTreeResponse |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_forks**
> [Repository] list_forks(owner, repo)

List a repository's forks

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.repository import Repository
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List a repository's forks
        api_response = api_instance.list_forks(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->list_forks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List a repository's forks
        api_response = api_instance.list_forks(owner, repo, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->list_forks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[Repository]**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RepositoryList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_add_collaborator**
> repo_add_collaborator(owner, repo, collaborator)

Add a collaborator to a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.add_collaborator_option import AddCollaboratorOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    collaborator = "collaborator_example" # str | username of the collaborator to add
    body = AddCollaboratorOption(
        permission="permission_example",
    ) # AddCollaboratorOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a collaborator to a repository
        api_instance.repo_add_collaborator(owner, repo, collaborator)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_add_collaborator: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a collaborator to a repository
        api_instance.repo_add_collaborator(owner, repo, collaborator, body=body)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_add_collaborator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **collaborator** | **str**| username of the collaborator to add |
 **body** | [**AddCollaboratorOption**](AddCollaboratorOption.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_add_team**
> repo_add_team(owner, repo, team)

Add a team to a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    team = "team_example" # str | team name

    # example passing only required values which don't have defaults set
    try:
        # Add a team to a repository
        api_instance.repo_add_team(owner, repo, team)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_add_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **team** | **str**| team name |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**405** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_add_topc**
> repo_add_topc(owner, repo, topic)

Add a topic to a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    topic = "topic_example" # str | name of the topic to add

    # example passing only required values which don't have defaults set
    try:
        # Add a topic to a repository
        api_instance.repo_add_topc(owner, repo, topic)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_add_topc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **topic** | **str**| name of the topic to add |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**422** | APIInvalidTopicsError is error format response to invalid topics |  * invalidTopics -  <br>  * message -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_check_collaborator**
> repo_check_collaborator(owner, repo, collaborator)

Check if a user is a collaborator of a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    collaborator = "collaborator_example" # str | username of the collaborator

    # example passing only required values which don't have defaults set
    try:
        # Check if a user is a collaborator of a repository
        api_instance.repo_check_collaborator(owner, repo, collaborator)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_check_collaborator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **collaborator** | **str**| username of the collaborator |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_check_team**
> Team repo_check_team(owner, repo, team)

Check if a team is assigned to a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.team import Team
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    team = "team_example" # str | team name

    # example passing only required values which don't have defaults set
    try:
        # Check if a team is assigned to a repository
        api_response = api_instance.repo_check_team(owner, repo, team)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_check_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **team** | **str**| team name |

### Return type

[**Team**](Team.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team |  -  |
**404** | APINotFound is a not found empty response |  -  |
**405** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_branch**
> Branch repo_create_branch(owner, repo)

Create a branch

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.create_branch_repo_option import CreateBranchRepoOption
from gitea.model.branch import Branch
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    body = CreateBranchRepoOption(
        new_branch_name="new_branch_name_example",
        old_branch_name="old_branch_name_example",
    ) # CreateBranchRepoOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a branch
        api_response = api_instance.repo_create_branch(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_branch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a branch
        api_response = api_instance.repo_create_branch(owner, repo, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_branch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**CreateBranchRepoOption**](CreateBranchRepoOption.md)|  | [optional]

### Return type

[**Branch**](Branch.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Branch |  -  |
**404** | The old branch does not exist. |  -  |
**409** | The branch with the same name already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_branch_protection**
> BranchProtection repo_create_branch_protection(owner, repo)

Create a branch protections for a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.create_branch_protection_option import CreateBranchProtectionOption
from gitea.model.branch_protection import BranchProtection
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    body = CreateBranchProtectionOption(
        approvals_whitelist_teams=[
            "approvals_whitelist_teams_example",
        ],
        approvals_whitelist_username=[
            "approvals_whitelist_username_example",
        ],
        block_on_official_review_requests=True,
        block_on_outdated_branch=True,
        block_on_rejected_reviews=True,
        branch_name="branch_name_example",
        dismiss_stale_approvals=True,
        enable_approvals_whitelist=True,
        enable_merge_whitelist=True,
        enable_push=True,
        enable_push_whitelist=True,
        enable_status_check=True,
        merge_whitelist_teams=[
            "merge_whitelist_teams_example",
        ],
        merge_whitelist_usernames=[
            "merge_whitelist_usernames_example",
        ],
        protected_file_patterns="protected_file_patterns_example",
        push_whitelist_deploy_keys=True,
        push_whitelist_teams=[
            "push_whitelist_teams_example",
        ],
        push_whitelist_usernames=[
            "push_whitelist_usernames_example",
        ],
        require_signed_commits=True,
        required_approvals=1,
        status_check_contexts=[
            "status_check_contexts_example",
        ],
    ) # CreateBranchProtectionOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a branch protections for a repository
        api_response = api_instance.repo_create_branch_protection(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_branch_protection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a branch protections for a repository
        api_response = api_instance.repo_create_branch_protection(owner, repo, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_branch_protection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**CreateBranchProtectionOption**](CreateBranchProtectionOption.md)|  | [optional]

### Return type

[**BranchProtection**](BranchProtection.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | BranchProtection |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_file**
> FileResponse repo_create_file(owner, repo, filepath, body)

Create a file in a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.create_file_options import CreateFileOptions
from gitea.model.file_response import FileResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    filepath = "filepath_example" # str | path of the file to create
    body = CreateFileOptions(
        author=Identity(
            email="email_example",
            name="name_example",
        ),
        branch="branch_example",
        committer=Identity(
            email="email_example",
            name="name_example",
        ),
        content="content_example",
        dates=CommitDateOptions(
            author=dateutil_parser('1970-01-01T00:00:00.00Z'),
            committer=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        message="message_example",
        new_branch="new_branch_example",
        signoff=True,
    ) # CreateFileOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Create a file in a repository
        api_response = api_instance.repo_create_file(owner, repo, filepath, body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **filepath** | **str**| path of the file to create |
 **body** | [**CreateFileOptions**](CreateFileOptions.md)|  |

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | FileResponse |  -  |
**403** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_hook**
> Hook repo_create_hook(owner, repo)

Create a hook

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.hook import Hook
from gitea.model.create_hook_option import CreateHookOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    body = CreateHookOption(
        active=False,
        branch_filter="branch_filter_example",
        config=CreateHookOptionConfig(
            key="key_example",
        ),
        events=[
            "events_example",
        ],
        type="dingtalk",
    ) # CreateHookOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a hook
        api_response = api_instance.repo_create_hook(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_hook: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a hook
        api_response = api_instance.repo_create_hook(owner, repo, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**CreateHookOption**](CreateHookOption.md)|  | [optional]

### Return type

[**Hook**](Hook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Hook |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_key**
> DeployKey repo_create_key(owner, repo)

Add a key to a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.deploy_key import DeployKey
from gitea.model.create_key_option import CreateKeyOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    body = CreateKeyOption(
        key="key_example",
        read_only=True,
        title="title_example",
    ) # CreateKeyOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a key to a repository
        api_response = api_instance.repo_create_key(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a key to a repository
        api_response = api_instance.repo_create_key(owner, repo, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**CreateKeyOption**](CreateKeyOption.md)|  | [optional]

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | DeployKey |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_pull_request**
> PullRequest repo_create_pull_request(owner, repo)

Create a pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.create_pull_request_option import CreatePullRequestOption
from gitea.model.pull_request import PullRequest
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    body = CreatePullRequestOption(
        assignee="assignee_example",
        assignees=[
            "assignees_example",
        ],
        base="base_example",
        body="body_example",
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        head="head_example",
        labels=[
            1,
        ],
        milestone=1,
        title="title_example",
    ) # CreatePullRequestOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a pull request
        api_response = api_instance.repo_create_pull_request(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_pull_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a pull request
        api_response = api_instance.repo_create_pull_request(owner, repo, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_pull_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**CreatePullRequestOption**](CreatePullRequestOption.md)|  | [optional]

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PullRequest |  -  |
**409** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_pull_review**
> PullReview repo_create_pull_review(owner, repo, index, body)

Create a review to an pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.create_pull_review_options import CreatePullReviewOptions
from gitea.model.pull_review import PullReview
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request
    body = CreatePullReviewOptions(
        body="body_example",
        comments=[
            CreatePullReviewComment(
                body="body_example",
                new_position=1,
                old_position=1,
                path="path_example",
            ),
        ],
        commit_id="commit_id_example",
        event="event_example",
    ) # CreatePullReviewOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Create a review to an pull request
        api_response = api_instance.repo_create_pull_review(owner, repo, index, body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_pull_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request |
 **body** | [**CreatePullReviewOptions**](CreatePullReviewOptions.md)|  |

### Return type

[**PullReview**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullReview |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_pull_review_requests**
> [PullReview] repo_create_pull_review_requests(owner, repo, index, body)

create review requests for a pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.pull_review_request_options import PullReviewRequestOptions
from gitea.model.pull_review import PullReview
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request
    body = PullReviewRequestOptions(
        reviewers=[
            "reviewers_example",
        ],
        team_reviewers=[
            "team_reviewers_example",
        ],
    ) # PullReviewRequestOptions | 

    # example passing only required values which don't have defaults set
    try:
        # create review requests for a pull request
        api_response = api_instance.repo_create_pull_review_requests(owner, repo, index, body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_pull_review_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request |
 **body** | [**PullReviewRequestOptions**](PullReviewRequestOptions.md)|  |

### Return type

[**[PullReview]**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PullReviewList |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_release**
> Release repo_create_release(owner, repo)

Create a release

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.create_release_option import CreateReleaseOption
from gitea.model.release import Release
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    body = CreateReleaseOption(
        body="body_example",
        draft=True,
        name="name_example",
        prerelease=True,
        tag_name="tag_name_example",
        target_commitish="target_commitish_example",
    ) # CreateReleaseOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a release
        api_response = api_instance.repo_create_release(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_release: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a release
        api_response = api_instance.repo_create_release(owner, repo, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**CreateReleaseOption**](CreateReleaseOption.md)|  | [optional]

### Return type

[**Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Release |  -  |
**404** | APINotFound is a not found empty response |  -  |
**409** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_release_attachment**
> Attachment repo_create_release_attachment(owner, repo, id, attachment)

Create a release attachment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.attachment import Attachment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the release
    attachment = open('/path/to/file', 'rb') # file_type | attachment to upload
    name = "name_example" # str | name of the attachment (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a release attachment
        api_response = api_instance.repo_create_release_attachment(owner, repo, id, attachment)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_release_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a release attachment
        api_response = api_instance.repo_create_release_attachment(owner, repo, id, attachment, name=name)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_release_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the release |
 **attachment** | **file_type**| attachment to upload |
 **name** | **str**| name of the attachment | [optional]

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attachment |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_create_status**
> CommitStatus repo_create_status(owner, repo, sha)

Create a commit status

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.commit_status import CommitStatus
from gitea.model.create_status_option import CreateStatusOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    sha = "sha_example" # str | sha of the commit
    body = CreateStatusOption(
        context="context_example",
        description="description_example",
        state="state_example",
        target_url="target_url_example",
    ) # CreateStatusOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a commit status
        api_response = api_instance.repo_create_status(owner, repo, sha)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a commit status
        api_response = api_instance.repo_create_status(owner, repo, sha, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_create_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **sha** | **str**| sha of the commit |
 **body** | [**CreateStatusOption**](CreateStatusOption.md)|  | [optional]

### Return type

[**CommitStatus**](CommitStatus.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CommitStatus |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete**
> repo_delete(owner, repo)

Delete a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo to delete
    repo = "repo_example" # str | name of the repo to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a repository
        api_instance.repo_delete(owner, repo)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to delete |
 **repo** | **str**| name of the repo to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_branch**
> repo_delete_branch(owner, repo, branch)

Delete a specific branch from a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    branch = "branch_example" # str | branch to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a specific branch from a repository
        api_instance.repo_delete_branch(owner, repo, branch)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_branch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **branch** | **str**| branch to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_branch_protection**
> repo_delete_branch_protection(owner, repo, name)

Delete a specific branch protection for the repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    name = "name_example" # str | name of protected branch

    # example passing only required values which don't have defaults set
    try:
        # Delete a specific branch protection for the repository
        api_instance.repo_delete_branch_protection(owner, repo, name)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_branch_protection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **name** | **str**| name of protected branch |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_collaborator**
> repo_delete_collaborator(owner, repo, collaborator)

Delete a collaborator from a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    collaborator = "collaborator_example" # str | username of the collaborator to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a collaborator from a repository
        api_instance.repo_delete_collaborator(owner, repo, collaborator)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_collaborator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **collaborator** | **str**| username of the collaborator to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_file**
> FileDeleteResponse repo_delete_file(owner, repo, filepath, body)

Delete a file in a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.file_delete_response import FileDeleteResponse
from gitea.model.delete_file_options import DeleteFileOptions
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    filepath = "filepath_example" # str | path of the file to delete
    body = DeleteFileOptions(
        author=Identity(
            email="email_example",
            name="name_example",
        ),
        branch="branch_example",
        committer=Identity(
            email="email_example",
            name="name_example",
        ),
        dates=CommitDateOptions(
            author=dateutil_parser('1970-01-01T00:00:00.00Z'),
            committer=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        message="message_example",
        new_branch="new_branch_example",
        sha="sha_example",
        signoff=True,
    ) # DeleteFileOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a file in a repository
        api_response = api_instance.repo_delete_file(owner, repo, filepath, body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **filepath** | **str**| path of the file to delete |
 **body** | [**DeleteFileOptions**](DeleteFileOptions.md)|  |

### Return type

[**FileDeleteResponse**](FileDeleteResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FileDeleteResponse |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_git_hook**
> repo_delete_git_hook(owner, repo, id)

Delete a Git hook in a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = "id_example" # str | id of the hook to get

    # example passing only required values which don't have defaults set
    try:
        # Delete a Git hook in a repository
        api_instance.repo_delete_git_hook(owner, repo, id)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_git_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **str**| id of the hook to get |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_hook**
> repo_delete_hook(owner, repo, id)

Delete a hook in a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the hook to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a hook in a repository
        api_instance.repo_delete_hook(owner, repo, id)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the hook to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_key**
> repo_delete_key(owner, repo, id)

Delete a key from a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the key to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a key from a repository
        api_instance.repo_delete_key(owner, repo, id)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the key to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_pull_review**
> repo_delete_pull_review(owner, repo, index, id)

Delete a specific review from a pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request
    id = 1 # int | id of the review

    # example passing only required values which don't have defaults set
    try:
        # Delete a specific review from a pull request
        api_instance.repo_delete_pull_review(owner, repo, index, id)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_pull_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request |
 **id** | **int**| id of the review |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_pull_review_requests**
> repo_delete_pull_review_requests(owner, repo, index, body)

cancel review requests for a pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.pull_review_request_options import PullReviewRequestOptions
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request
    body = PullReviewRequestOptions(
        reviewers=[
            "reviewers_example",
        ],
        team_reviewers=[
            "team_reviewers_example",
        ],
    ) # PullReviewRequestOptions | 

    # example passing only required values which don't have defaults set
    try:
        # cancel review requests for a pull request
        api_instance.repo_delete_pull_review_requests(owner, repo, index, body)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_pull_review_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request |
 **body** | [**PullReviewRequestOptions**](PullReviewRequestOptions.md)|  |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_release**
> repo_delete_release(owner, repo, id)

Delete a release

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the release to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a release
        api_instance.repo_delete_release(owner, repo, id)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the release to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_release_attachment**
> repo_delete_release_attachment(owner, repo, id, attachment_id)

Delete a release attachment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the release
    attachment_id = 1 # int | id of the attachment to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a release attachment
        api_instance.repo_delete_release_attachment(owner, repo, id, attachment_id)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_release_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the release |
 **attachment_id** | **int**| id of the attachment to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_release_by_tag**
> repo_delete_release_by_tag(owner, repo, tag)

Delete a release by tag name

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    tag = "tag_example" # str | tag name of the release to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a release by tag name
        api_instance.repo_delete_release_by_tag(owner, repo, tag)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_release_by_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **tag** | **str**| tag name of the release to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_tag**
> repo_delete_tag(owner, repo, tag)

Delete a repository's tag by name

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    tag = "tag_example" # str | name of tag to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a repository's tag by name
        api_instance.repo_delete_tag(owner, repo, tag)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **tag** | **str**| name of tag to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**409** | APIConflict is a conflict empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_team**
> repo_delete_team(owner, repo, team)

Delete a team from a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    team = "team_example" # str | team name

    # example passing only required values which don't have defaults set
    try:
        # Delete a team from a repository
        api_instance.repo_delete_team(owner, repo, team)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_team: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **team** | **str**| team name |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**405** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_delete_topic**
> repo_delete_topic(owner, repo, topic)

Delete a topic from a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    topic = "topic_example" # str | name of the topic to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete a topic from a repository
        api_instance.repo_delete_topic(owner, repo, topic)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_delete_topic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **topic** | **str**| name of the topic to delete |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**422** | APIInvalidTopicsError is error format response to invalid topics |  * invalidTopics -  <br>  * message -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_dismiss_pull_review**
> PullReview repo_dismiss_pull_review(owner, repo, index, id, body)

Dismiss a review for a pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.dismiss_pull_review_options import DismissPullReviewOptions
from gitea.model.pull_review import PullReview
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request
    id = 1 # int | id of the review
    body = DismissPullReviewOptions(
        message="message_example",
    ) # DismissPullReviewOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Dismiss a review for a pull request
        api_response = api_instance.repo_dismiss_pull_review(owner, repo, index, id, body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_dismiss_pull_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request |
 **id** | **int**| id of the review |
 **body** | [**DismissPullReviewOptions**](DismissPullReviewOptions.md)|  |

### Return type

[**PullReview**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullReview |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_download_pull_diff**
> str repo_download_pull_diff(owner, repo, index)

Get a pull request diff

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request to get

    # example passing only required values which don't have defaults set
    try:
        # Get a pull request diff
        api_response = api_instance.repo_download_pull_diff(owner, repo, index)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_download_pull_diff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request to get |

### Return type

**str**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIString is a string response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_download_pull_patch**
> str repo_download_pull_patch(owner, repo, index)

Get a pull request patch file

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request to get

    # example passing only required values which don't have defaults set
    try:
        # Get a pull request patch file
        api_response = api_instance.repo_download_pull_patch(owner, repo, index)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_download_pull_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request to get |

### Return type

**str**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIString is a string response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit**
> Repository repo_edit(owner, repo)

Edit a repository's properties. Only fields that are set will be changed.

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.repository import Repository
from gitea.model.edit_repo_option import EditRepoOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo to edit
    repo = "repo_example" # str | name of the repo to edit
    body = EditRepoOption(
        allow_manual_merge=True,
        allow_merge_commits=True,
        allow_rebase=True,
        allow_rebase_explicit=True,
        allow_squash_merge=True,
        archived=True,
        autodetect_manual_merge=True,
        default_branch="default_branch_example",
        description="description_example",
        external_tracker=ExternalTracker(
            external_tracker_format="external_tracker_format_example",
            external_tracker_style="external_tracker_style_example",
            external_tracker_url="external_tracker_url_example",
        ),
        external_wiki=ExternalWiki(
            external_wiki_url="external_wiki_url_example",
        ),
        has_issues=True,
        has_projects=True,
        has_pull_requests=True,
        has_wiki=True,
        ignore_whitespace_conflicts=True,
        internal_tracker=InternalTracker(
            allow_only_contributors_to_track_time=True,
            enable_issue_dependencies=True,
            enable_time_tracker=True,
        ),
        mirror_interval="mirror_interval_example",
        name="name_example",
        private=True,
        template=True,
        website="website_example",
    ) # EditRepoOption | Properties of a repo that you can edit (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a repository's properties. Only fields that are set will be changed.
        api_response = api_instance.repo_edit(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a repository's properties. Only fields that are set will be changed.
        api_response = api_instance.repo_edit(owner, repo, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to edit |
 **repo** | **str**| name of the repo to edit |
 **body** | [**EditRepoOption**](EditRepoOption.md)| Properties of a repo that you can edit | [optional]

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_branch_protection**
> BranchProtection repo_edit_branch_protection(owner, repo, name)

Edit a branch protections for a repository. Only fields that are set will be changed

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.branch_protection import BranchProtection
from gitea.model.edit_branch_protection_option import EditBranchProtectionOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    name = "name_example" # str | name of protected branch
    body = EditBranchProtectionOption(
        approvals_whitelist_teams=[
            "approvals_whitelist_teams_example",
        ],
        approvals_whitelist_username=[
            "approvals_whitelist_username_example",
        ],
        block_on_official_review_requests=True,
        block_on_outdated_branch=True,
        block_on_rejected_reviews=True,
        dismiss_stale_approvals=True,
        enable_approvals_whitelist=True,
        enable_merge_whitelist=True,
        enable_push=True,
        enable_push_whitelist=True,
        enable_status_check=True,
        merge_whitelist_teams=[
            "merge_whitelist_teams_example",
        ],
        merge_whitelist_usernames=[
            "merge_whitelist_usernames_example",
        ],
        protected_file_patterns="protected_file_patterns_example",
        push_whitelist_deploy_keys=True,
        push_whitelist_teams=[
            "push_whitelist_teams_example",
        ],
        push_whitelist_usernames=[
            "push_whitelist_usernames_example",
        ],
        require_signed_commits=True,
        required_approvals=1,
        status_check_contexts=[
            "status_check_contexts_example",
        ],
    ) # EditBranchProtectionOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a branch protections for a repository. Only fields that are set will be changed
        api_response = api_instance.repo_edit_branch_protection(owner, repo, name)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit_branch_protection: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a branch protections for a repository. Only fields that are set will be changed
        api_response = api_instance.repo_edit_branch_protection(owner, repo, name, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit_branch_protection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **name** | **str**| name of protected branch |
 **body** | [**EditBranchProtectionOption**](EditBranchProtectionOption.md)|  | [optional]

### Return type

[**BranchProtection**](BranchProtection.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BranchProtection |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_git_hook**
> GitHook repo_edit_git_hook(owner, repo, id)

Edit a Git hook in a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.git_hook import GitHook
from gitea.model.edit_git_hook_option import EditGitHookOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = "id_example" # str | id of the hook to get
    body = EditGitHookOption(
        content="content_example",
    ) # EditGitHookOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a Git hook in a repository
        api_response = api_instance.repo_edit_git_hook(owner, repo, id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit_git_hook: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a Git hook in a repository
        api_response = api_instance.repo_edit_git_hook(owner, repo, id, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit_git_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **str**| id of the hook to get |
 **body** | [**EditGitHookOption**](EditGitHookOption.md)|  | [optional]

### Return type

[**GitHook**](GitHook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GitHook |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_hook**
> Hook repo_edit_hook(owner, repo, id)

Edit a hook in a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.hook import Hook
from gitea.model.edit_hook_option import EditHookOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | index of the hook
    body = EditHookOption(
        active=True,
        branch_filter="branch_filter_example",
        config={
            "key": "key_example",
        },
        events=[
            "events_example",
        ],
    ) # EditHookOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a hook in a repository
        api_response = api_instance.repo_edit_hook(owner, repo, id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit_hook: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a hook in a repository
        api_response = api_instance.repo_edit_hook(owner, repo, id, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| index of the hook |
 **body** | [**EditHookOption**](EditHookOption.md)|  | [optional]

### Return type

[**Hook**](Hook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hook |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_pull_request**
> PullRequest repo_edit_pull_request(owner, repo, index)

Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.edit_pull_request_option import EditPullRequestOption
from gitea.model.pull_request import PullRequest
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request to edit
    body = EditPullRequestOption(
        assignee="assignee_example",
        assignees=[
            "assignees_example",
        ],
        base="base_example",
        body="body_example",
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        labels=[
            1,
        ],
        milestone=1,
        state="state_example",
        title="title_example",
        unset_due_date=True,
    ) # EditPullRequestOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.repo_edit_pull_request(owner, repo, index)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit_pull_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.
        api_response = api_instance.repo_edit_pull_request(owner, repo, index, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit_pull_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request to edit |
 **body** | [**EditPullRequestOption**](EditPullRequestOption.md)|  | [optional]

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | PullRequest |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**409** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**412** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_release**
> Release repo_edit_release(owner, repo, id)

Update a release

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.edit_release_option import EditReleaseOption
from gitea.model.release import Release
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the release to edit
    body = EditReleaseOption(
        body="body_example",
        draft=True,
        name="name_example",
        prerelease=True,
        tag_name="tag_name_example",
        target_commitish="target_commitish_example",
    ) # EditReleaseOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a release
        api_response = api_instance.repo_edit_release(owner, repo, id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit_release: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a release
        api_response = api_instance.repo_edit_release(owner, repo, id, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the release to edit |
 **body** | [**EditReleaseOption**](EditReleaseOption.md)|  | [optional]

### Return type

[**Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_edit_release_attachment**
> Attachment repo_edit_release_attachment(owner, repo, id, attachment_id)

Edit a release attachment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.attachment import Attachment
from gitea.model.edit_attachment_options import EditAttachmentOptions
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the release
    attachment_id = 1 # int | id of the attachment to edit
    body = EditAttachmentOptions(
        name="name_example",
    ) # EditAttachmentOptions |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a release attachment
        api_response = api_instance.repo_edit_release_attachment(owner, repo, id, attachment_id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit_release_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a release attachment
        api_response = api_instance.repo_edit_release_attachment(owner, repo, id, attachment_id, body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_edit_release_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the release |
 **attachment_id** | **int**| id of the attachment to edit |
 **body** | [**EditAttachmentOptions**](EditAttachmentOptions.md)|  | [optional]

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get**
> Repository repo_get(owner, repo)

Get a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.repository import Repository
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo

    # example passing only required values which don't have defaults set
    try:
        # Get a repository
        api_response = api_instance.repo_get(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_all_commits**
> [Commit] repo_get_all_commits(owner, repo)

Get a list of all commits from a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.commit import Commit
from gitea.model.api_error import APIError
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    sha = "sha_example" # str | SHA or branch to start listing commits from (usually 'master') (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a list of all commits from a repository
        api_response = api_instance.repo_get_all_commits(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_all_commits: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a list of all commits from a repository
        api_response = api_instance.repo_get_all_commits(owner, repo, sha=sha, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_all_commits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **sha** | **str**| SHA or branch to start listing commits from (usually &#39;master&#39;) | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[Commit]**](Commit.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommitList |  * X-HasMore - True if there is another page <br>  * X-PageCount - Total number of pages <br>  * X-PerPage - Commits per page <br>  * X-Total - Total commit count <br>  * X-Page - The current page <br>  |
**404** | APINotFound is a not found empty response |  -  |
**409** | EmptyRepository |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_archive**
> repo_get_archive(owner, repo, archive)

Get an archive of a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    archive = "archive_example" # str | the git reference for download with attached archive format (e.g. master.zip)

    # example passing only required values which don't have defaults set
    try:
        # Get an archive of a repository
        api_instance.repo_get_archive(owner, repo, archive)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_archive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **archive** | **str**| the git reference for download with attached archive format (e.g. master.zip) |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_branch**
> Branch repo_get_branch(owner, repo, branch)

Retrieve a specific branch from a repository, including its effective branch protection

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.branch import Branch
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    branch = "branch_example" # str | branch to get

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a specific branch from a repository, including its effective branch protection
        api_response = api_instance.repo_get_branch(owner, repo, branch)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_branch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **branch** | **str**| branch to get |

### Return type

[**Branch**](Branch.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Branch |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_branch_protection**
> BranchProtection repo_get_branch_protection(owner, repo, name)

Get a specific branch protection for the repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.branch_protection import BranchProtection
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    name = "name_example" # str | name of protected branch

    # example passing only required values which don't have defaults set
    try:
        # Get a specific branch protection for the repository
        api_response = api_instance.repo_get_branch_protection(owner, repo, name)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_branch_protection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **name** | **str**| name of protected branch |

### Return type

[**BranchProtection**](BranchProtection.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BranchProtection |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_by_id**
> Repository repo_get_by_id(id)

Get a repository by id

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.repository import Repository
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    id = 1 # int | id of the repo to get

    # example passing only required values which don't have defaults set
    try:
        # Get a repository by id
        api_response = api_instance.repo_get_by_id(id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the repo to get |

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_combined_status_by_ref**
> CombinedStatus repo_get_combined_status_by_ref(owner, repo, ref)

Get a commit's combined status, by branch/tag/commit reference

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.combined_status import CombinedStatus
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    ref = "ref_example" # str | name of branch/tag/commit
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a commit's combined status, by branch/tag/commit reference
        api_response = api_instance.repo_get_combined_status_by_ref(owner, repo, ref)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_combined_status_by_ref: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a commit's combined status, by branch/tag/commit reference
        api_response = api_instance.repo_get_combined_status_by_ref(owner, repo, ref, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_combined_status_by_ref: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **ref** | **str**| name of branch/tag/commit |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**CombinedStatus**](CombinedStatus.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CombinedStatus |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_contents**
> ContentsResponse repo_get_contents(owner, repo, filepath)

Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.contents_response import ContentsResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    filepath = "filepath_example" # str | path of the dir, file, symlink or submodule in the repo
    ref = "ref_example" # str | The name of the commit/branch/tag. Default the repository’s default branch (usually master) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir
        api_response = api_instance.repo_get_contents(owner, repo, filepath)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_contents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir
        api_response = api_instance.repo_get_contents(owner, repo, filepath, ref=ref)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_contents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **filepath** | **str**| path of the dir, file, symlink or submodule in the repo |
 **ref** | **str**| The name of the commit/branch/tag. Default the repository’s default branch (usually master) | [optional]

### Return type

[**ContentsResponse**](ContentsResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContentsResponse |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_contents_list**
> [ContentsResponse] repo_get_contents_list(owner, repo)

Gets the metadata of all the entries of the root dir

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.contents_response import ContentsResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    ref = "ref_example" # str | The name of the commit/branch/tag. Default the repository’s default branch (usually master) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the metadata of all the entries of the root dir
        api_response = api_instance.repo_get_contents_list(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_contents_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the metadata of all the entries of the root dir
        api_response = api_instance.repo_get_contents_list(owner, repo, ref=ref)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_contents_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **ref** | **str**| The name of the commit/branch/tag. Default the repository’s default branch (usually master) | [optional]

### Return type

[**[ContentsResponse]**](ContentsResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ContentsListResponse |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_editor_config**
> repo_get_editor_config(owner, repo, filepath)

Get the EditorConfig definitions of a file in a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    filepath = "filepath_example" # str | filepath of file to get

    # example passing only required values which don't have defaults set
    try:
        # Get the EditorConfig definitions of a file in a repository
        api_instance.repo_get_editor_config(owner, repo, filepath)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_editor_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **filepath** | **str**| filepath of file to get |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_git_hook**
> GitHook repo_get_git_hook(owner, repo, id)

Get a Git hook

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.git_hook import GitHook
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = "id_example" # str | id of the hook to get

    # example passing only required values which don't have defaults set
    try:
        # Get a Git hook
        api_response = api_instance.repo_get_git_hook(owner, repo, id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_git_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **str**| id of the hook to get |

### Return type

[**GitHook**](GitHook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GitHook |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_hook**
> Hook repo_get_hook(owner, repo, id)

Get a hook

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.hook import Hook
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the hook to get

    # example passing only required values which don't have defaults set
    try:
        # Get a hook
        api_response = api_instance.repo_get_hook(owner, repo, id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the hook to get |

### Return type

[**Hook**](Hook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hook |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_issue_templates**
> [IssueTemplate] repo_get_issue_templates(owner, repo)

Get available issue templates for a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.issue_template import IssueTemplate
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo

    # example passing only required values which don't have defaults set
    try:
        # Get available issue templates for a repository
        api_response = api_instance.repo_get_issue_templates(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_issue_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |

### Return type

[**[IssueTemplate]**](IssueTemplate.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IssueTemplates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_key**
> DeployKey repo_get_key(owner, repo, id)

Get a repository's key by id

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.deploy_key import DeployKey
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the key to get

    # example passing only required values which don't have defaults set
    try:
        # Get a repository's key by id
        api_response = api_instance.repo_get_key(owner, repo, id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the key to get |

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeployKey |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_languages**
> {str: (int,)} repo_get_languages(owner, repo)

Get languages and number of bytes of code written

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo

    # example passing only required values which don't have defaults set
    try:
        # Get languages and number of bytes of code written
        api_response = api_instance.repo_get_languages(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_languages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |

### Return type

**{str: (int,)}**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LanguageStatistics |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_pull_request**
> PullRequest repo_get_pull_request(owner, repo, index)

Get a pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.pull_request import PullRequest
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request to get

    # example passing only required values which don't have defaults set
    try:
        # Get a pull request
        api_response = api_instance.repo_get_pull_request(owner, repo, index)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_pull_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request to get |

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullRequest |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_pull_review**
> PullReview repo_get_pull_review(owner, repo, index, id)

Get a specific review for a pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.pull_review import PullReview
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request
    id = 1 # int | id of the review

    # example passing only required values which don't have defaults set
    try:
        # Get a specific review for a pull request
        api_response = api_instance.repo_get_pull_review(owner, repo, index, id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_pull_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request |
 **id** | **int**| id of the review |

### Return type

[**PullReview**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullReview |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_pull_review_comments**
> [PullReviewComment] repo_get_pull_review_comments(owner, repo, index, id)

Get a specific review for a pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.pull_review_comment import PullReviewComment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request
    id = 1 # int | id of the review

    # example passing only required values which don't have defaults set
    try:
        # Get a specific review for a pull request
        api_response = api_instance.repo_get_pull_review_comments(owner, repo, index, id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_pull_review_comments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request |
 **id** | **int**| id of the review |

### Return type

[**[PullReviewComment]**](PullReviewComment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullCommentList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_raw_file**
> repo_get_raw_file(owner, repo, filepath)

Get a file from a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    filepath = "filepath_example" # str | filepath of the file to get
    ref = "ref_example" # str | The name of the commit/branch/tag. Default the repository’s default branch (usually master) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a file from a repository
        api_instance.repo_get_raw_file(owner, repo, filepath)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_raw_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a file from a repository
        api_instance.repo_get_raw_file(owner, repo, filepath, ref=ref)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_raw_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **filepath** | **str**| filepath of the file to get |
 **ref** | **str**| The name of the commit/branch/tag. Default the repository’s default branch (usually master) | [optional]

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_release**
> Release repo_get_release(owner, repo, id)

Get a release

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.release import Release
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the release to get

    # example passing only required values which don't have defaults set
    try:
        # Get a release
        api_response = api_instance.repo_get_release(owner, repo, id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_release: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the release to get |

### Return type

[**Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_release_attachment**
> Attachment repo_get_release_attachment(owner, repo, id, attachment_id)

Get a release attachment

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.attachment import Attachment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the release
    attachment_id = 1 # int | id of the attachment to get

    # example passing only required values which don't have defaults set
    try:
        # Get a release attachment
        api_response = api_instance.repo_get_release_attachment(owner, repo, id, attachment_id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_release_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the release |
 **attachment_id** | **int**| id of the attachment to get |

### Return type

[**Attachment**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_release_by_tag**
> Release repo_get_release_by_tag(owner, repo, tag)

Get a release by tag name

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.release import Release
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    tag = "tag_example" # str | tag name of the release to get

    # example passing only required values which don't have defaults set
    try:
        # Get a release by tag name
        api_response = api_instance.repo_get_release_by_tag(owner, repo, tag)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_release_by_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **tag** | **str**| tag name of the release to get |

### Return type

[**Release**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Release |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_get_single_commit**
> Commit repo_get_single_commit(owner, repo, sha)

Get a single commit from a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.commit import Commit
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    sha = "sha_example" # str | a git ref or commit sha

    # example passing only required values which don't have defaults set
    try:
        # Get a single commit from a repository
        api_response = api_instance.repo_get_single_commit(owner, repo, sha)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_get_single_commit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **sha** | **str**| a git ref or commit sha |

### Return type

[**Commit**](Commit.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Commit |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_all_git_refs**
> [Reference] repo_list_all_git_refs(owner, repo)

Get specified ref or filtered repository's refs

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.reference import Reference
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo

    # example passing only required values which don't have defaults set
    try:
        # Get specified ref or filtered repository's refs
        api_response = api_instance.repo_list_all_git_refs(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_all_git_refs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |

### Return type

[**[Reference]**](Reference.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReferenceList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_branch_protection**
> [BranchProtection] repo_list_branch_protection(owner, repo)

List branch protections for a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.branch_protection import BranchProtection
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo

    # example passing only required values which don't have defaults set
    try:
        # List branch protections for a repository
        api_response = api_instance.repo_list_branch_protection(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_branch_protection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |

### Return type

[**[BranchProtection]**](BranchProtection.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BranchProtectionList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_branches**
> [Branch] repo_list_branches(owner, repo)

List a repository's branches

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.branch import Branch
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List a repository's branches
        api_response = api_instance.repo_list_branches(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_branches: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List a repository's branches
        api_response = api_instance.repo_list_branches(owner, repo, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_branches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[Branch]**](Branch.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BranchList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_collaborators**
> [User] repo_list_collaborators(owner, repo)

List a repository's collaborators

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List a repository's collaborators
        api_response = api_instance.repo_list_collaborators(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_collaborators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List a repository's collaborators
        api_response = api_instance.repo_list_collaborators(owner, repo, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_collaborators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[User]**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_git_hooks**
> [GitHook] repo_list_git_hooks(owner, repo)

List the Git hooks in a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.git_hook import GitHook
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo

    # example passing only required values which don't have defaults set
    try:
        # List the Git hooks in a repository
        api_response = api_instance.repo_list_git_hooks(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_git_hooks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |

### Return type

[**[GitHook]**](GitHook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GitHookList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_git_refs**
> [Reference] repo_list_git_refs(owner, repo, ref)

Get specified ref or filtered repository's refs

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.reference import Reference
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    ref = "ref_example" # str | part or full name of the ref

    # example passing only required values which don't have defaults set
    try:
        # Get specified ref or filtered repository's refs
        api_response = api_instance.repo_list_git_refs(owner, repo, ref)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_git_refs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **ref** | **str**| part or full name of the ref |

### Return type

[**[Reference]**](Reference.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReferenceList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_hooks**
> [Hook] repo_list_hooks(owner, repo)

List the hooks in a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.hook import Hook
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List the hooks in a repository
        api_response = api_instance.repo_list_hooks(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_hooks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the hooks in a repository
        api_response = api_instance.repo_list_hooks(owner, repo, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_hooks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[Hook]**](Hook.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HookList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_keys**
> [DeployKey] repo_list_keys(owner, repo)

List a repository's keys

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.deploy_key import DeployKey
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    key_id = 1 # int | the key_id to search for (optional)
    fingerprint = "fingerprint_example" # str | fingerprint of the key (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List a repository's keys
        api_response = api_instance.repo_list_keys(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_keys: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List a repository's keys
        api_response = api_instance.repo_list_keys(owner, repo, key_id=key_id, fingerprint=fingerprint, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **key_id** | **int**| the key_id to search for | [optional]
 **fingerprint** | **str**| fingerprint of the key | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[DeployKey]**](DeployKey.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | DeployKeyList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_pull_requests**
> [PullRequest] repo_list_pull_requests(owner, repo)

List a repo's pull requests

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.pull_request import PullRequest
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    state = "closed" # str | State of pull request: open or closed (optional) (optional)
    sort = "oldest" # str | Type of sort (optional)
    milestone = 1 # int | ID of the milestone (optional)
    labels = [
        1,
    ] # [int] | Label IDs (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List a repo's pull requests
        api_response = api_instance.repo_list_pull_requests(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_pull_requests: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List a repo's pull requests
        api_response = api_instance.repo_list_pull_requests(owner, repo, state=state, sort=sort, milestone=milestone, labels=labels, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_pull_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **state** | **str**| State of pull request: open or closed (optional) | [optional]
 **sort** | **str**| Type of sort | [optional]
 **milestone** | **int**| ID of the milestone | [optional]
 **labels** | **[int]**| Label IDs | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[PullRequest]**](PullRequest.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullRequestList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_pull_reviews**
> [PullReview] repo_list_pull_reviews(owner, repo, index)

List all reviews for a pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.pull_review import PullReview
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all reviews for a pull request
        api_response = api_instance.repo_list_pull_reviews(owner, repo, index)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_pull_reviews: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all reviews for a pull request
        api_response = api_instance.repo_list_pull_reviews(owner, repo, index, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_pull_reviews: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[PullReview]**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullReviewList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_release_attachments**
> [Attachment] repo_list_release_attachments(owner, repo, id)

List release's attachments

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.attachment import Attachment
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the release

    # example passing only required values which don't have defaults set
    try:
        # List release's attachments
        api_response = api_instance.repo_list_release_attachments(owner, repo, id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_release_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the release |

### Return type

[**[Attachment]**](Attachment.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AttachmentList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_releases**
> [Release] repo_list_releases(owner, repo)

List a repo's releases

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.release import Release
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    per_page = 1 # int | page size of results, deprecated - use limit (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List a repo's releases
        api_response = api_instance.repo_list_releases(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_releases: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List a repo's releases
        api_response = api_instance.repo_list_releases(owner, repo, per_page=per_page, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_releases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **per_page** | **int**| page size of results, deprecated - use limit | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[Release]**](Release.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ReleaseList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_stargazers**
> [User] repo_list_stargazers(owner, repo)

List a repo's stargazers

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List a repo's stargazers
        api_response = api_instance.repo_list_stargazers(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_stargazers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List a repo's stargazers
        api_response = api_instance.repo_list_stargazers(owner, repo, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_stargazers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[User]**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_statuses**
> [CommitStatus] repo_list_statuses(owner, repo, sha)

Get a commit's statuses

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.commit_status import CommitStatus
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    sha = "sha_example" # str | sha of the commit
    sort = "oldest" # str | type of sort (optional)
    state = "pending" # str | type of state (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a commit's statuses
        api_response = api_instance.repo_list_statuses(owner, repo, sha)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_statuses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a commit's statuses
        api_response = api_instance.repo_list_statuses(owner, repo, sha, sort=sort, state=state, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_statuses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **sha** | **str**| sha of the commit |
 **sort** | **str**| type of sort | [optional]
 **state** | **str**| type of state | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[CommitStatus]**](CommitStatus.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommitStatusList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_statuses_by_ref**
> [CommitStatus] repo_list_statuses_by_ref(owner, repo, ref)

Get a commit's statuses, by branch/tag/commit reference

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.commit_status import CommitStatus
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    ref = "ref_example" # str | name of branch/tag/commit
    sort = "oldest" # str | type of sort (optional)
    state = "pending" # str | type of state (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a commit's statuses, by branch/tag/commit reference
        api_response = api_instance.repo_list_statuses_by_ref(owner, repo, ref)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_statuses_by_ref: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a commit's statuses, by branch/tag/commit reference
        api_response = api_instance.repo_list_statuses_by_ref(owner, repo, ref, sort=sort, state=state, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_statuses_by_ref: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **ref** | **str**| name of branch/tag/commit |
 **sort** | **str**| type of sort | [optional]
 **state** | **str**| type of state | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[CommitStatus]**](CommitStatus.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommitStatusList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_subscribers**
> [User] repo_list_subscribers(owner, repo)

List a repo's watchers

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.user import User
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List a repo's watchers
        api_response = api_instance.repo_list_subscribers(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_subscribers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List a repo's watchers
        api_response = api_instance.repo_list_subscribers(owner, repo, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[User]**](User.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_tags**
> [Tag] repo_list_tags(owner, repo)

List a repository's tags

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.tag import Tag
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results, default maximum page size is 50 (optional)

    # example passing only required values which don't have defaults set
    try:
        # List a repository's tags
        api_response = api_instance.repo_list_tags(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List a repository's tags
        api_response = api_instance.repo_list_tags(owner, repo, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results, default maximum page size is 50 | [optional]

### Return type

[**[Tag]**](Tag.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TagList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_teams**
> [Team] repo_list_teams(owner, repo)

List a repository's teams

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.team import Team
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo

    # example passing only required values which don't have defaults set
    try:
        # List a repository's teams
        api_response = api_instance.repo_list_teams(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_teams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |

### Return type

[**[Team]**](Team.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TeamList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_list_topics**
> TopicName repo_list_topics(owner, repo)

Get list of topics that a repository has

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.topic_name import TopicName
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get list of topics that a repository has
        api_response = api_instance.repo_list_topics(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_topics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get list of topics that a repository has
        api_response = api_instance.repo_list_topics(owner, repo, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_list_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**TopicName**](TopicName.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TopicNames |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_merge_pull_request**
> repo_merge_pull_request(owner, repo, index)

Merge a pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.merge_pull_request_option import MergePullRequestOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request to merge
    body = MergePullRequestOption(
        do="merge",
        merge_commit_id="merge_commit_id_example",
        merge_message_field="merge_message_field_example",
        merge_title_field="merge_title_field_example",
        force_merge=True,
    ) # MergePullRequestOption |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Merge a pull request
        api_instance.repo_merge_pull_request(owner, repo, index)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_merge_pull_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Merge a pull request
        api_instance.repo_merge_pull_request(owner, repo, index, body=body)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_merge_pull_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request to merge |
 **body** | [**MergePullRequestOption**](MergePullRequestOption.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIEmpty is an empty response |  -  |
**405** | APIEmpty is an empty response |  -  |
**409** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_migrate**
> Repository repo_migrate()

Migrate a remote git repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.repository import Repository
from gitea.model.migrate_repo_options import MigrateRepoOptions
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    body = MigrateRepoOptions(
        auth_password="auth_password_example",
        auth_token="auth_token_example",
        auth_username="auth_username_example",
        clone_addr="clone_addr_example",
        description="description_example",
        issues=True,
        labels=True,
        milestones=True,
        mirror=True,
        mirror_interval="mirror_interval_example",
        private=True,
        pull_requests=True,
        releases=True,
        repo_name="repo_name_example",
        repo_owner="repo_owner_example",
        service="git",
        uid=1,
        wiki=True,
    ) # MigrateRepoOptions |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Migrate a remote git repository
        api_response = api_instance.repo_migrate(body=body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_migrate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MigrateRepoOptions**](MigrateRepoOptions.md)|  | [optional]

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Repository |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_mirror_sync**
> repo_mirror_sync(owner, repo)

Sync a mirrored repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo to sync
    repo = "repo_example" # str | name of the repo to sync

    # example passing only required values which don't have defaults set
    try:
        # Sync a mirrored repository
        api_instance.repo_mirror_sync(owner, repo)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_mirror_sync: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to sync |
 **repo** | **str**| name of the repo to sync |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_pull_request_is_merged**
> repo_pull_request_is_merged(owner, repo, index)

Check if a pull request has been merged

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request

    # example passing only required values which don't have defaults set
    try:
        # Check if a pull request has been merged
        api_instance.repo_pull_request_is_merged(owner, repo, index)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_pull_request_is_merged: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | pull request has been merged |  -  |
**404** | pull request has not been merged |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_search**
> SearchResults repo_search()

Search for repositories

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.search_results import SearchResults
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    q = "q_example" # str | keyword (optional)
    topic = True # bool | Limit search to repositories with keyword as topic (optional)
    include_desc = True # bool | include search of keyword within repository description (optional)
    uid = 1 # int | search only for repos that the user with the given id owns or contributes to (optional)
    priority_owner_id = 1 # int | repo owner to prioritize in the results (optional)
    team_id = 1 # int | search only for repos that belong to the given team id (optional)
    starred_by = 1 # int | search only for repos that the user with the given id has starred (optional)
    private = True # bool | include private repositories this user has access to (defaults to true) (optional)
    is_private = True # bool | show only pubic, private or all repositories (defaults to all) (optional)
    template = True # bool | include template repositories this user has access to (defaults to true) (optional)
    archived = True # bool | show only archived, non-archived or all repositories (defaults to all) (optional)
    mode = "mode_example" # str | type of repository to search for. Supported values are \"fork\", \"source\", \"mirror\" and \"collaborative\" (optional)
    exclusive = True # bool | if `uid` is given, search only for repos that the user owns (optional)
    sort = "sort_example" # str | sort repos by attribute. Supported values are \"alpha\", \"created\", \"updated\", \"size\", and \"id\". Default is \"alpha\" (optional)
    order = "order_example" # str | sort order, either \"asc\" (ascending) or \"desc\" (descending). Default is \"asc\", ignored if \"sort\" is not specified. (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for repositories
        api_response = api_instance.repo_search(q=q, topic=topic, include_desc=include_desc, uid=uid, priority_owner_id=priority_owner_id, team_id=team_id, starred_by=starred_by, private=private, is_private=is_private, template=template, archived=archived, mode=mode, exclusive=exclusive, sort=sort, order=order, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| keyword | [optional]
 **topic** | **bool**| Limit search to repositories with keyword as topic | [optional]
 **include_desc** | **bool**| include search of keyword within repository description | [optional]
 **uid** | **int**| search only for repos that the user with the given id owns or contributes to | [optional]
 **priority_owner_id** | **int**| repo owner to prioritize in the results | [optional]
 **team_id** | **int**| search only for repos that belong to the given team id | [optional]
 **starred_by** | **int**| search only for repos that the user with the given id has starred | [optional]
 **private** | **bool**| include private repositories this user has access to (defaults to true) | [optional]
 **is_private** | **bool**| show only pubic, private or all repositories (defaults to all) | [optional]
 **template** | **bool**| include template repositories this user has access to (defaults to true) | [optional]
 **archived** | **bool**| show only archived, non-archived or all repositories (defaults to all) | [optional]
 **mode** | **str**| type of repository to search for. Supported values are \&quot;fork\&quot;, \&quot;source\&quot;, \&quot;mirror\&quot; and \&quot;collaborative\&quot; | [optional]
 **exclusive** | **bool**| if &#x60;uid&#x60; is given, search only for repos that the user owns | [optional]
 **sort** | **str**| sort repos by attribute. Supported values are \&quot;alpha\&quot;, \&quot;created\&quot;, \&quot;updated\&quot;, \&quot;size\&quot;, and \&quot;id\&quot;. Default is \&quot;alpha\&quot; | [optional]
 **order** | **str**| sort order, either \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending). Default is \&quot;asc\&quot;, ignored if \&quot;sort\&quot; is not specified. | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SearchResults |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_signing_key**
> str repo_signing_key(owner, repo)

Get signing-key.gpg for given repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo

    # example passing only required values which don't have defaults set
    try:
        # Get signing-key.gpg for given repository
        api_response = api_instance.repo_signing_key(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_signing_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |

### Return type

**str**

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GPG armored public key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_submit_pull_review**
> PullReview repo_submit_pull_review(owner, repo, index, id, body)

Submit a pending review to an pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.submit_pull_review_options import SubmitPullReviewOptions
from gitea.model.pull_review import PullReview
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request
    id = 1 # int | id of the review
    body = SubmitPullReviewOptions(
        body="body_example",
        event="event_example",
    ) # SubmitPullReviewOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Submit a pending review to an pull request
        api_response = api_instance.repo_submit_pull_review(owner, repo, index, id, body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_submit_pull_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request |
 **id** | **int**| id of the review |
 **body** | [**SubmitPullReviewOptions**](SubmitPullReviewOptions.md)|  |

### Return type

[**PullReview**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullReview |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_test_hook**
> repo_test_hook(owner, repo, id)

Test a push webhook

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    id = 1 # int | id of the hook to test

    # example passing only required values which don't have defaults set
    try:
        # Test a push webhook
        api_instance.repo_test_hook(owner, repo, id)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_test_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **id** | **int**| id of the hook to test |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_tracked_times**
> [TrackedTime] repo_tracked_times(owner, repo)

List a repo's tracked times

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.tracked_time import TrackedTime
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    user = "user_example" # str | optional filter by user (available for issue managers) (optional)
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show times updated after the given time. This is a timestamp in RFC 3339 format (optional)
    before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Only show times updated before the given time. This is a timestamp in RFC 3339 format (optional)
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List a repo's tracked times
        api_response = api_instance.repo_tracked_times(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_tracked_times: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List a repo's tracked times
        api_response = api_instance.repo_tracked_times(owner, repo, user=user, since=since, before=before, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_tracked_times: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **user** | **str**| optional filter by user (available for issue managers) | [optional]
 **since** | **datetime**| Only show times updated after the given time. This is a timestamp in RFC 3339 format | [optional]
 **before** | **datetime**| Only show times updated before the given time. This is a timestamp in RFC 3339 format | [optional]
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[TrackedTime]**](TrackedTime.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TrackedTimeList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_transfer**
> Repository repo_transfer(owner, repo, body)

Transfer a repo ownership

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.repository import Repository
from gitea.model.transfer_repo_option import TransferRepoOption
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo to transfer
    repo = "repo_example" # str | name of the repo to transfer
    body = TransferRepoOption(
        new_owner="new_owner_example",
        team_ids=[
            1,
        ],
    ) # TransferRepoOption | Transfer Options

    # example passing only required values which don't have defaults set
    try:
        # Transfer a repo ownership
        api_response = api_instance.repo_transfer(owner, repo, body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_transfer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo to transfer |
 **repo** | **str**| name of the repo to transfer |
 **body** | [**TransferRepoOption**](TransferRepoOption.md)| Transfer Options |

### Return type

[**Repository**](Repository.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Repository |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_un_dismiss_pull_review**
> PullReview repo_un_dismiss_pull_review(owner, repo, index, id)

Cancel to dismiss a review for a pull request

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.pull_review import PullReview
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request
    id = 1 # int | id of the review

    # example passing only required values which don't have defaults set
    try:
        # Cancel to dismiss a review for a pull request
        api_response = api_instance.repo_un_dismiss_pull_review(owner, repo, index, id)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_un_dismiss_pull_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request |
 **id** | **int**| id of the review |

### Return type

[**PullReview**](PullReview.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PullReview |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_update_file**
> FileResponse repo_update_file(owner, repo, filepath, body)

Update a file in a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.file_response import FileResponse
from gitea.model.update_file_options import UpdateFileOptions
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    filepath = "filepath_example" # str | path of the file to update
    body = UpdateFileOptions(
        author=Identity(
            email="email_example",
            name="name_example",
        ),
        branch="branch_example",
        committer=Identity(
            email="email_example",
            name="name_example",
        ),
        content="content_example",
        dates=CommitDateOptions(
            author=dateutil_parser('1970-01-01T00:00:00.00Z'),
            committer=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        from_path="from_path_example",
        message="message_example",
        new_branch="new_branch_example",
        sha="sha_example",
        signoff=True,
    ) # UpdateFileOptions | 

    # example passing only required values which don't have defaults set
    try:
        # Update a file in a repository
        api_response = api_instance.repo_update_file(owner, repo, filepath, body)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_update_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **filepath** | **str**| path of the file to update |
 **body** | [**UpdateFileOptions**](UpdateFileOptions.md)|  |

### Return type

[**FileResponse**](FileResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FileResponse |  -  |
**403** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIError is error format response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_update_pull_request**
> repo_update_pull_request(owner, repo, index)

Merge PR's baseBranch into headBranch

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    index = 1 # int | index of the pull request to get

    # example passing only required values which don't have defaults set
    try:
        # Merge PR's baseBranch into headBranch
        api_instance.repo_update_pull_request(owner, repo, index)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_update_pull_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **index** | **int**| index of the pull request to get |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**409** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repo_update_topics**
> repo_update_topics(owner, repo)

Replace list of topics for a repository

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.repo_topic_options import RepoTopicOptions
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    body = RepoTopicOptions(
        topics=[
            "topics_example",
        ],
    ) # RepoTopicOptions |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replace list of topics for a repository
        api_instance.repo_update_topics(owner, repo)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_update_topics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replace list of topics for a repository
        api_instance.repo_update_topics(owner, repo, body=body)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->repo_update_topics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **body** | [**RepoTopicOptions**](RepoTopicOptions.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**422** | APIInvalidTopicsError is error format response to invalid topics |  * invalidTopics -  <br>  * message -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topic_search**
> [TopicResponse] topic_search(q)

search topics via keyword

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.topic_response import TopicResponse
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    q = "q_example" # str | keywords to search
    page = 1 # int | page number of results to return (1-based) (optional)
    limit = 1 # int | page size of results (optional)

    # example passing only required values which don't have defaults set
    try:
        # search topics via keyword
        api_response = api_instance.topic_search(q)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->topic_search: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # search topics via keyword
        api_response = api_instance.topic_search(q, page=page, limit=limit)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->topic_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| keywords to search |
 **page** | **int**| page number of results to return (1-based) | [optional]
 **limit** | **int**| page size of results | [optional]

### Return type

[**[TopicResponse]**](TopicResponse.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TopicListResponse |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_current_check_subscription**
> WatchInfo user_current_check_subscription(owner, repo)

Check if the current user is watching a repo

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.watch_info import WatchInfo
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo

    # example passing only required values which don't have defaults set
    try:
        # Check if the current user is watching a repo
        api_response = api_instance.user_current_check_subscription(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->user_current_check_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |

### Return type

[**WatchInfo**](WatchInfo.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WatchInfo |  -  |
**404** | User is not watching this repo or repo do not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_current_delete_subscription**
> user_current_delete_subscription(owner, repo)

Unwatch a repo

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo

    # example passing only required values which don't have defaults set
    try:
        # Unwatch a repo
        api_instance.user_current_delete_subscription(owner, repo)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->user_current_delete_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |

### Return type

void (empty response body)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_current_put_subscription**
> WatchInfo user_current_put_subscription(owner, repo)

Watch a repo

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.watch_info import WatchInfo
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo

    # example passing only required values which don't have defaults set
    try:
        # Watch a repo
        api_response = api_instance.user_current_put_subscription(owner, repo)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->user_current_put_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |

### Return type

[**WatchInfo**](WatchInfo.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WatchInfo |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_tracked_times**
> [TrackedTime] user_tracked_times(owner, repo, user)

List a user's tracked times in a repo

### Example

* Api Key Authentication (AccessToken):
* Api Key Authentication (AuthorizationHeaderToken):
* Basic Authentication (BasicAuth):
* Api Key Authentication (SudoHeader):
* Api Key Authentication (SudoParam):
* Api Key Authentication (TOTPHeader):
* Api Key Authentication (Token):

```python
import time
import gitea
from gitea.api import repository_api
from gitea.model.tracked_time import TrackedTime
from pprint import pprint
# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = repository_api.RepositoryApi(api_client)
    owner = "owner_example" # str | owner of the repo
    repo = "repo_example" # str | name of the repo
    user = "user_example" # str | username of user

    # example passing only required values which don't have defaults set
    try:
        # List a user's tracked times in a repo
        api_response = api_instance.user_tracked_times(owner, repo, user)
        pprint(api_response)
    except gitea.ApiException as e:
        print("Exception when calling RepositoryApi->user_tracked_times: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| owner of the repo |
 **repo** | **str**| name of the repo |
 **user** | **str**| username of user |

### Return type

[**[TrackedTime]**](TrackedTime.md)

### Authorization

[AccessToken](../README.md#AccessToken), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [BasicAuth](../README.md#BasicAuth), [SudoHeader](../README.md#SudoHeader), [SudoParam](../README.md#SudoParam), [TOTPHeader](../README.md#TOTPHeader), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TrackedTimeList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

