from rest_framework.response import Response
from rest_framework import status
from templated_mail.mail import BaseEmailMessage


def send_email(request):
    message = BaseEmailMessage(
        template_name= 'emails/hellow.html',
        context= {'name': 'Reza'}
    )
    message.send(['to@domain.com'])
    return Response({'message': 'ایمیل با موفقیت ارسال شد.'}, status=status.HTTP_200_OK)
