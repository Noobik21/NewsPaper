from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User

@shared_task
def send_news_notification(email, title):
    send_mail(
        subject=f'Новая новость: {title}',
        message='Появилась новая новость!',
        from_email='your@email.com',
        recipient_list=[email],
    )

@shared_task
def send_weekly_news():
    from .models import Post
    from django.utils import timezone
    from datetime import timedelta

    last_week = timezone.now() - timedelta(days=7)
    Post = Post.objects.filter(created_at__gte=last_week)

    for user in User.objects.all():
        send_mail(
            subject='Новости за неделю',
            message='\n'.join([n.title for n in Post]),
            from_email='your@email.com',
            recipient_list=[user.email],
        )