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
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.username

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        return result
