from django.core.mail import send_mail
from celery.decorators import task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@task(name="send_email")
def send_user_email(username, password):
    logger.info("Send email")
    send_mail(
        'Witam serdecznie',
        f'Twój username to {username} a haslo to {password}',
        'witam',
        ['jakubszkodny@gmail.com'],
    )

