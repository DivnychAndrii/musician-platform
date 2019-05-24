from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives


@shared_task
def notify_recipient(title, message, author, requester):
    requester = get_user_model().objects.get(id=requester)
    author = get_user_model().objects.get(id=author)
    mail_message = f'You have one request from {requester.email} - {message}'
    mail = EmailMultiAlternatives(title, mail_message, to=[author.email])
    mail.attach_alternative(mail_message, 'text/html')
    mail.send()
