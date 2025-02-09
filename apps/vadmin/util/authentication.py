import logging

import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.utils.six import text_type
from django.utils.translation import ugettext as _
from rest_framework import exceptions
from rest_framework_jwt.utils import jwt_decode_handler

from apps.vadmin.permission.models import UserProfile
from apps.vadmin.util.jwt_util import jwt_get_session_id

logger = logging.getLogger(__name__)
User = get_user_model()


class OpAuthJwtAuthentication(object):
    def authenticate(self, request):
        token = self.get_header_authorization(request) or self.get_cookie_authorization(request)
        if not token:
            return None
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            msg = _('Signature has expired.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()
        except UserProfile.DoesNotExist:
            raise exceptions.AuthenticationFailed()

        username = payload.get('username', None)
        if not username:
            return None
        username_field = settings.USERNAME_FIELD or 'username'
        user = User.objects.filter(**{username_field: username}).first()
        if not user or not user.is_active:
            return None
        return user, token

    def authenticate_header(self, request):
        pass

    @classmethod
    def get_header_authorization(cls, request):
        auth = request.META.get('HTTP_AUTHORIZATION', b'')
        if isinstance(auth, text_type):
            auth = auth.encode(settings.JWT_AUTH.get('HTTP_HEADER_ENCODING', 'iso-8859-1'))
        if not auth:
            return ''
        auth = str(auth, encoding='utf-8').split()
        if len(auth) != 2 or auth[0].upper() != settings.JWT_AUTH.get('JWT_AUTH_HEADER_PREFIX', 'JWT').upper():
            return ''
        return auth[1]

    @classmethod
    def get_cookie_authorization(cls, request):
        auth = request.COOKIES.get(settings.JWT_AUTH.get('JWT_AUTH_COOKIE', 'AUTH_JWT'), '')
        auth = auth.split()
        if len(auth) != 2 or auth[0].upper() != settings.JWT_AUTH.get('JWT_AUTH_HEADER_PREFIX', 'JWT'):
            return ''
        return auth[1]


class RedisOpAuthJwtAuthentication(OpAuthJwtAuthentication):
    prefix = settings.JWT_AUTH.get('JWT_AUTH_HEADER_PREFIX', 'JWT')

    def authenticate(self, request):
        res = super().authenticate(request)
        if res and getattr(settings, "REDIS_ENABLE", False):
            user, token = res
            session_id = jwt_get_session_id(token)
            key = f"{self.prefix}_{session_id}_{user.username}"
            redis_token = cache.get(key)
            if redis_token == token:
                return user, token
            else:
                raise exceptions.AuthenticationFailed("Thông tin đăng nhập không hợp lệ, vui lòng đăng nhập lại！")
        return res
