#!/usr/bin/python
import re
import random
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os
"""Functions"""


def is_valid_email(email):
    """Validates an email"""
    # Regular expression for a simple email validation
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    # Check if the provided email matches the pattern
    return bool(re.match(email_pattern, email))


def generate_otp():
    return random.randint(100000, 999999)


def send_email():
    """Sends verification email"""
    u_email = os.getenv('USER_MAIL')
    otp_token = os.getenv('USER_TOKEN')
    e_subject = 'Email verification'
    e_message = 'Here is your verification code to authenticate your account\n\t{}'.format(otp_token)
    send_mail(subject=e_subject,
              message=e_message,
              recipient_list=[u_email],
              from_email=None,
              fail_silently=False
              )


def send_cool_mail():
    """send email with cool html templates"""
    e_subject = 'Email verification'
    u_email = os.getenv('USER_MAIL')
    otp_token = os.getenv('USER_TOKEN')
    html_message = render_to_string("email_temp.html")
    plain = strip_tags(html_message)

    messages = EmailMultiAlternatives(
        subject=e_subject,
        body=plain,
        from_email=None,
        to=u_email,
    )
    messages.attach_alternative(html_message, 'text/html')
    messages.send()

