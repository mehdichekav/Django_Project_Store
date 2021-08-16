from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from core.models import BaseModel
from .managers import MyUserManager
from django.db.models.signals import post_save

from django.utils.translation import gettext as _


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('first_name'),
                                  help_text=_('enter your first_name'))
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('last_name'),
                                 help_text=_('enter your last_name'))
    email = models.CharField(max_length=100, unique=True, verbose_name=_('Email'), help_text=_('enter your email'))
    phone = models.CharField(max_length=100, verbose_name=_('phone'), help_text=_('enter your phone'))
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_('date_of_birth'),
                                     help_text=_('enter your date_of_birth'))
    is_active = models.BooleanField(default=True)
    objects = MyUserManager()
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return str(self.first_name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


# class Register(User):
#    pass
#
# class Edit_Customer(User):
#     pass

class Address(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', verbose_name=_('owner'), help_text=_('enter your owner'))
    lat = models.FloatField(blank=True, null=True, verbose_name=_('lat'), help_text=_('enter your lat'))
    lng = models.FloatField(blank=True, null=True, verbose_name=_('lng'), help_text=_('enter your lng'))
    country = models.CharField(max_length=50, verbose_name=_('country'), help_text=_('enter your country'))
    city = models.CharField(max_length=50, verbose_name=_('city'), help_text=_('enter your city'))
    State = models.CharField(max_length=50, verbose_name=_('state'), help_text=_('enter your state'))  # استان
    description = models.TextField(blank=True, null=True, verbose_name=_('description'),
                                   help_text=_('enter your description'))  # مشخصات دقیق آدرس
    zip_code = models.CharField(max_length=50, verbose_name=_('zip_code'), help_text=_('enter your zop_cide'))
    Alley = models.CharField(max_length=50, verbose_name=_('Alley'), help_text=_('enter your Alley'))  # کوچه
    Plaque = models.CharField(max_length=50, verbose_name=_('plaque'), help_text=_('enter your plaque'))  # پلاک

    # class Meta:
    #     ordering = ('city',)
    #     verbose_name_plural = 'Address'

    def __str__(self):
        return str(self.owner)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user'))
    phone = models.CharField(max_length=100, verbose_name=_('phone'), help_text=_('enter your phone'))
    address = models.TextField(verbose_name=_('address'),
                                   help_text=_('enter your address'), null=True, blank=True)

    def __str__(self):
        return str(self.user)


def save_profile_user(sender, **kwargs):
    if kwargs['created']:
        profile_user = Profile(user=kwargs['instance'])
        profile_user.save()


post_save.connect(save_profile_user, sender=User)
