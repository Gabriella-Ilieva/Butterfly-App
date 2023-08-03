from django.contrib.auth import get_user_model
from django.db import models

from butterfly.initiatives.models import Initiative

UserModel = get_user_model()


class Comment(models.Model):
    comment_text = models.TextField(max_length=300, blank=False, null=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE, )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        ordering = ('-date_time_of_publication',)
