from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from butterfly import settings
from core.email_utils import send_email_with_template

UserModel = get_user_model()


def send_successful_registration_email(user):
    context = {
        'user': user,
    }
    send_email_with_template(
        subject='Welcome to Butterfly world',
        template_name='email/registration.html',
        context=context,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email,)
    )


@receiver(post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        send_successful_registration_email(instance)
