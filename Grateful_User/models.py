from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.utils import timezone

class CustomUserManager(UserManager):
    """ユーザーマネージャー"""
    use_in_migrations = True

    def _create_user(self,thanks_id,password, **extra_fields):
        if not thanks_id:
            raise ValueError('The given employee_id must be set')
        #mail_address = self.normalize_email(mail_address)
        user = self.model(thanks_id=thanks_id , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,thanks_id, password=None,  **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(thanks_id,password, **extra_fields)

    def create_superuser(self,thanks_id, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(thanks_id,password,  **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(verbose_name='お名前',null=False,max_length=30)
    email = models.EmailField(verbose_name='メールアドレス',null=True)
    thanks_id=models.CharField(verbose_name='user_name',primary_key=True,null=False,unique=True,max_length=50)
    grateful_to_count=models.PositiveIntegerField(verbose_name='感謝した回数',default=0)
    be_grateful_count=models.PositiveIntegerField(verbose_name='感謝された回数',default=0)

    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'mail_address'
    USERNAME_FIELD = 'thanks_id'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'user'

    def get_thanks_id(self):
        return '@'+self.thanks_id

    def get_grateful_to(self):
        return self.grateful_to_count

    def get_be_grateful_count(self):
        return self.be_grateful_count

    @property
    def username(self):
        return '@'+self.thanks_id

