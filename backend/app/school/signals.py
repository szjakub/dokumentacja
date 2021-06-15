from django.conf import settings
from django.db.models.signals import post_save, pre_save, post_init
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import School
from .tasks import send_user_email
from .utils import username_generator, password_generator


User = get_user_model()


@receiver(post_save, sender=School)
def send_email_with_school_creds(sender, instance=None, created=False, **kwargs):
    username = username_generator(str(instance.principal_email))
    password = password_generator(username)
    if created:
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
    if instance.verified and not instance.email_sent:
        send_user_email.delay(username, password)


