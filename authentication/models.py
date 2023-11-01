
from django.contrib.postgres.fields import ArrayField
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self,last_name ,username,first_name, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email),last_name=last_name,first_name=first_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, blank=True, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    password = models.CharField(max_length=128)
    data_created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def token(self):
        return self._generate_jwt_token()
    
    def get_full_name(self):
        return (self.first_name,self.last_name)
    
    def get_short_name(self):
        return self.username
    
    def _generate_jwt_token(self):
        print(self)
        """
           Генерирует веб-токен JSON, в котором хранится идентификатор этого
           пользователя, срок действия токена составляет 30 день от создания
           """
        dt = datetime.now() + timedelta(days=30)
       
        token = jwt.encode({
           'id': self.pk,
           # Используйте timestamp для правильного форматирования времени
          }, settings.SECRET_KEY, algorithm='HS256')

        return token.encode('utf-8')
       