# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from gitea.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from gitea.model.api_error import APIError
from gitea.model.access_token import AccessToken
from gitea.model.add_collaborator_option import AddCollaboratorOption
from gitea.model.add_time_option import AddTimeOption
from gitea.model.annotated_tag import AnnotatedTag
from gitea.model.annotated_tag_object import AnnotatedTagObject
from gitea.model.attachment import Attachment
from gitea.model.branch import Branch
from gitea.model.branch_protection import BranchProtection
from gitea.model.combined_status import CombinedStatus
from gitea.model.comment import Comment
from gitea.model.commit import Commit
from gitea.model.commit_affected_files import CommitAffectedFiles
from gitea.model.commit_date_options import CommitDateOptions
from gitea.model.commit_meta import CommitMeta
from gitea.model.commit_status import CommitStatus
from gitea.model.commit_user import CommitUser
from gitea.model.contents_response import ContentsResponse
from gitea.model.create_branch_protection_option import CreateBranchProtectionOption
from gitea.model.create_branch_repo_option import CreateBranchRepoOption
from gitea.model.create_email_option import CreateEmailOption
from gitea.model.create_file_options import CreateFileOptions
from gitea.model.create_fork_option import CreateForkOption
from gitea.model.create_gpg_key_option import CreateGPGKeyOption
from gitea.model.create_hook_option import CreateHookOption
from gitea.model.create_hook_option_config import CreateHookOptionConfig
from gitea.model.create_issue_comment_option import CreateIssueCommentOption
from gitea.model.create_issue_option import CreateIssueOption
from gitea.model.create_key_option import CreateKeyOption
from gitea.model.create_label_option import CreateLabelOption
from gitea.model.create_milestone_option import CreateMilestoneOption
from gitea.model.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from gitea.model.create_org_option import CreateOrgOption
from gitea.model.create_pull_request_option import CreatePullRequestOption
from gitea.model.create_pull_review_comment import CreatePullReviewComment
from gitea.model.create_pull_review_options import CreatePullReviewOptions
from gitea.model.create_release_option import CreateReleaseOption
from gitea.model.create_repo_option import CreateRepoOption
from gitea.model.create_status_option import CreateStatusOption
from gitea.model.create_team_option import CreateTeamOption
from gitea.model.create_user_option import CreateUserOption
from gitea.model.cron import Cron
from gitea.model.delete_email_option import DeleteEmailOption
from gitea.model.delete_file_options import DeleteFileOptions
from gitea.model.deploy_key import DeployKey
from gitea.model.dismiss_pull_review_options import DismissPullReviewOptions
from gitea.model.edit_attachment_options import EditAttachmentOptions
from gitea.model.edit_branch_protection_option import EditBranchProtectionOption
from gitea.model.edit_deadline_option import EditDeadlineOption
from gitea.model.edit_git_hook_option import EditGitHookOption
from gitea.model.edit_hook_option import EditHookOption
from gitea.model.edit_issue_comment_option import EditIssueCommentOption
from gitea.model.edit_issue_option import EditIssueOption
from gitea.model.edit_label_option import EditLabelOption
from gitea.model.edit_milestone_option import EditMilestoneOption
from gitea.model.edit_org_option import EditOrgOption
from gitea.model.edit_pull_request_option import EditPullRequestOption
from gitea.model.edit_reaction_option import EditReactionOption
from gitea.model.edit_release_option import EditReleaseOption
from gitea.model.edit_repo_option import EditRepoOption
from gitea.model.edit_team_option import EditTeamOption
from gitea.model.edit_user_option import EditUserOption
from gitea.model.email import Email
from gitea.model.external_tracker import ExternalTracker
from gitea.model.external_wiki import ExternalWiki
from gitea.model.file_commit_response import FileCommitResponse
from gitea.model.file_delete_response import FileDeleteResponse
from gitea.model.file_links_response import FileLinksResponse
from gitea.model.file_response import FileResponse
from gitea.model.gpg_key import GPGKey
from gitea.model.gpg_key_email import GPGKeyEmail
from gitea.model.general_api_settings import GeneralAPISettings
from gitea.model.general_attachment_settings import GeneralAttachmentSettings
from gitea.model.general_repo_settings import GeneralRepoSettings
from gitea.model.general_ui_settings import GeneralUISettings
from gitea.model.git_blob_response import GitBlobResponse
from gitea.model.git_entry import GitEntry
from gitea.model.git_hook import GitHook
from gitea.model.git_object import GitObject
from gitea.model.git_tree_response import GitTreeResponse
from gitea.model.hook import Hook
from gitea.model.identity import Identity
from gitea.model.internal_tracker import InternalTracker
from gitea.model.issue import Issue
from gitea.model.issue_deadline import IssueDeadline
from gitea.model.issue_labels_option import IssueLabelsOption
from gitea.model.issue_template import IssueTemplate
from gitea.model.label import Label
from gitea.model.markdown_option import MarkdownOption
from gitea.model.merge_pull_request_option import MergePullRequestOption
from gitea.model.migrate_repo_form import MigrateRepoForm
from gitea.model.migrate_repo_options import MigrateRepoOptions
from gitea.model.milestone import Milestone
from gitea.model.notification_count import NotificationCount
from gitea.model.notification_subject import NotificationSubject
from gitea.model.notification_thread import NotificationThread
from gitea.model.o_auth2_application import OAuth2Application
from gitea.model.organization import Organization
from gitea.model.pr_branch_info import PRBranchInfo
from gitea.model.payload_commit import PayloadCommit
from gitea.model.payload_commit_verification import PayloadCommitVerification
from gitea.model.payload_user import PayloadUser
from gitea.model.permission import Permission
from gitea.model.public_key import PublicKey
from gitea.model.pull_request import PullRequest
from gitea.model.pull_request_meta import PullRequestMeta
from gitea.model.pull_review import PullReview
from gitea.model.pull_review_comment import PullReviewComment
from gitea.model.pull_review_request_options import PullReviewRequestOptions
from gitea.model.reaction import Reaction
from gitea.model.reference import Reference
from gitea.model.release import Release
from gitea.model.repo_commit import RepoCommit
from gitea.model.repo_topic_options import RepoTopicOptions
from gitea.model.repository import Repository
from gitea.model.repository_meta import RepositoryMeta
from gitea.model.search_results import SearchResults
from gitea.model.server_version import ServerVersion
from gitea.model.stop_watch import StopWatch
from gitea.model.submit_pull_review_options import SubmitPullReviewOptions
from gitea.model.tag import Tag
from gitea.model.team import Team
from gitea.model.team_search200_response import TeamSearch200Response
from gitea.model.topic_name import TopicName
from gitea.model.topic_response import TopicResponse
from gitea.model.tracked_time import TrackedTime
from gitea.model.transfer_repo_option import TransferRepoOption
from gitea.model.update_file_options import UpdateFileOptions
from gitea.model.user import User
from gitea.model.user_create_token_request import UserCreateTokenRequest
from gitea.model.user_heatmap_data import UserHeatmapData
from gitea.model.user_search200_response import UserSearch200Response
from gitea.model.watch_info import WatchInfo