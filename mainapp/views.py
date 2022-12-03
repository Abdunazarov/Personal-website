from django.shortcuts import render
from django.contrib import messages

from django.core.mail import send_mail


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject=f"{name} left message in your personal website",
            message='',
            from_email='Personal Website <diyorchegg@gmail.com>',
            recipient_list=['diyorchegg@gmail.com'],
            auth_password='snktgjbsikpsvyal',
            fail_silently=False,
            html_message=f"<h2>{message}</h2>"
        )

        messages.success(request, 'Email has been sent successfully')

    return render(request, 'mainapp/home.html')


