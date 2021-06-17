from django.core.mail import send_mail
from celery.decorators import task
from celery.utils.log import get_task_logger
from .utils import render_template

logger = get_task_logger(__name__)


@task(name="new_school_email")
def new_school_created_email(to, school_name, school_address, username, password):
    context = {
        'school_name': school_name, 'school_address': school_address,
        'username': username, 'password': password
    }
    template = render_template('mail/new_school_email.html', context)

    logger.info(f"Sending email to {to}")
    send_mail('Witamy w aplikacji Cyprus', template, 'cyprus', [to])
