from django.conf import settings
from django.db.models.signals import post_save, pre_save, post_init
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from mail.tasks import new_school_created_email
from .models import School
from .utils import username_generator, password_generator


User = get_user_model()


@receiver(post_save, sender=School)
def send_email_with_school_creds(sender, instance=None, created=False, **kwargs):
    username = username_generator(str(instance.principal_email))
    password = password_generator(username)
    if created:
        user = User.objects.create(username=username)
        user.role = User.PRINCIPAL
        user.set_password(password)
        user.save()
    if instance.verified and not instance.email_sent:
        new_school_created_email.delay(
            instance.principal_email,
            instance.school_name,
            instance.school_address,
            username,
            password
        )


