from django.utils import timezone
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _
from drf_spectacular.extensions import OpenApiAuthenticationExtension
from .models import Authorization


class BearerTokenAuthentication(BaseAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    @classmethod
    def authenticate_credentials(cls, token):
        try:
            obj = Authorization.objects.get(token=token)
            if obj.expired_at < timezone.now():
                raise AuthenticationFailed(_('Token expired'))
        except Authorization.DoesNotExist:
            raise AuthenticationFailed(_('Invalid token.'))

        if not obj.user.is_active:
            raise AuthenticationFailed(_('User inactive or deleted.'))

        return obj.user, token

    def authenticate_header(self, request):
        return self.keyword


class BearerTokenAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = BearerTokenAuthentication
    name = 'BearerTokenAuthentication'

    def get_security_definition(self, auto_schema):
        return {
            'type': 'http',
            'scheme': 'bearer'
        }
