from django.core.mail import EmailMessage
from celery.decorators import task
from celery.utils.log import get_task_logger
from .utils import render_template

from project.settings import EMAIL_ADMIN

logger = get_task_logger(__name__)


@task(name="school_request_email")
def school_request_email(to, **context):
    message = render_template('mail/school_request_email.html', context)

    logger.info(f"Sending email to {to}")
    mail = EmailMessage(
        subject='Witamy w aplikacji Cyprus',
        body=message,
        from_email=EMAIL_ADMIN,
        to=[to]
    )
    mail.content_subtype = "html"
    return mail.send()


@task(name="school_created_email")
def school_created_email(to, **context):
    message = render_template('mail/school_created_email.html', context)

    logger.info(f"Sending email to {to}")
    mail = EmailMessage(
        subject='Rejestracja szkoły',
        body=message,
        from_email=EMAIL_ADMIN,
        to=[to]
    )
    mail.content_subtype = "html"
    return mail.send()
