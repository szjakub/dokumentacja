from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from mail.tasks import school_created_email
from users.utils import password_generator
from .models import School, Principal

User = get_user_model()


@receiver(post_save, sender=School)
def send_email_with_school_creds(sender, instance=None, **kwargs):
    if instance.verified and not instance.email_sent:
        principal = instance.school_principal.user
        password = password_generator()
        principal.set_password(password)
        principal.save()

        instance.email_sent = True
        instance.save()
        school_created_email.delay(
            to=principal.email,
            school_name=instance.school_name,
            school_address=instance.school_address,
            username=principal.username,
            password=password
        )
