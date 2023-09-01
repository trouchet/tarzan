from django.db.models import Model
from django.db.models import CharField, \
    TextField, \
    DateTimeField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Post(Model):
    title = CharField(max_length=200)
    content = TextField()
    pub_date = DateTimeField('date published')

    def __str__(self):
        return self.title
