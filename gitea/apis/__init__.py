
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from gitea.api.admin_api import AdminApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from gitea.api.admin_api import AdminApi
from gitea.api.issue_api import IssueApi
from gitea.api.miscellaneous_api import MiscellaneousApi
from gitea.api.notification_api import NotificationApi
from gitea.api.organization_api import OrganizationApi
from gitea.api.repository_api import RepositoryApi
from gitea.api.settings_api import SettingsApi
from gitea.api.user_api import UserApi
