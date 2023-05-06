from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import BooleanField, CharField, ManyToManyField
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel, SoftDeleteModel
from apps.task1.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel, SoftDeleteModel):
    username = None
    phone_number = PhoneNumberField(verbose_name=_("Phone number"), region="UZ", unique=True, primary_key=True)

    first_name = CharField(verbose_name=_("First name"), max_length=124)
    last_name = CharField(verbose_name=_("Last name"), max_length=124)

    is_deleted = BooleanField(default=False)
    is_staff = BooleanField(verbose_name=_("Is staff?"), default=False)
    is_active = BooleanField(verbose_name=_("Is active?"), default=True)
    is_superuser = BooleanField(verbose_name=_("Is superuser?"), default=False)

    groups = ManyToManyField(verbose_name=_("Groups"), to="auth.Group", related_name="task1", blank=True)

    objects = CustomUserManager()  # noqa F821

    USERNAME_FIELD = "phone_number" ""

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return str(self.phone_number)
