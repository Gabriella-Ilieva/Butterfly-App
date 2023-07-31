from django.contrib.auth import get_user_model
from django.db import models

from butterfly.validators import image_validator_5mb

UserModel = get_user_model()


class Story(models.Model):

    title = models.CharField(
        max_length=50,
    )

    description = models.TextField()
    image = models.URLField()
    # image = models.ImageField(
    #     validators=(
    #         image_validator_5mb,
    #     ),
    #     upload_to='story_imgs',
    # )
    date_of_publication = models.DateField(auto_now=True)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )
