from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

User = get_user_model()

class JWTAuthentication(BasicAuthentication):

    def authenticate(self, request):
        header = request.headers.get('Authorization')

        if not header:
            return None
        
        if not header.startswith('Bearer'):
            raise PermissionDenied(detail='Invalid Auth Token')
        
        token = header.replace('Bearer ', '')

        try:
            # create payload
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            # get user from payload sub
            user = User.objects.get(pk=payload.get('sub'))
            # print("USER -> ", user)

        # incase token has expired or is incorrect formatting
        except jwt.exceptions.InvalidTokenError:
            raise PermissionDenied(detail='Invalid Token')
        
        except User.DoesNotExist:
            raise PermissionDenied(detail="User not found")
        
        # if all good then return user & token
        return (user, token)
    