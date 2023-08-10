from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Story(models.Model):

    title = models.CharField(
        null=False,
        blank=False,
        max_length=50,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    image = models.URLField(
        null=True,
        blank=True,
    )
    date_of_publication = models.DateField(auto_now=True)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('-date_of_publication',)
