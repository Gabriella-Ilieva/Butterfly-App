from django.core import validators, exceptions
from django.db import models
from django.contrib.auth import models as auth_model


def profile_name_validator(value):
    if not value.isalpha():
        raise exceptions.ValidationError('Your name should contains only letters')


class ButterflyUser(auth_model.AbstractUser):
    FIRST_NAME_MAX_LENGTH = 20
    LAST_NAME_MAX_LENGTH = 30
    NAME_MIN_LEN = 2

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        verbose_name='First name',
        validators=(
            validators.MinLengthValidator(NAME_MIN_LEN),
            profile_name_validator,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        verbose_name='Last name',
        validators=(
            validators.MinLengthValidator(NAME_MIN_LEN),
            profile_name_validator,
        )
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        verbose_name='E-mail'
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name="Profile picture"
    )

