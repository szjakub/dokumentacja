from django.core.mail import send_mail
from celery.decorators import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@task(name="send_email")
def send_user_email():
    logger.info("Send email")
    send_mail(
        'Subject here',
        'Here is the message.',
        'jakubszkodny@pepisandbox.com',
        ['jakubszkodny@gmail.com'],
    )

