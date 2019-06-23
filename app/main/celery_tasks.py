from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives


# @shared_task
# def send_mail(user_id):
#     user = get_user_model().objects.filter(id=user_id)
#     user = user.first()
#     title = 'Verify'
#     mail_message = f'Follow this link to verify your account'
#     mail = EmailMultiAlternatives(title, mail_message, to=[user.email])
#     mail.attach_alternative(mail_message, mimetype=mail_message)
#     mail.send()
