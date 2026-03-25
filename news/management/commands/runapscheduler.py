from django.core.management.base import BaseCommand
from apscheduler.schedulers.blocking import BlockingScheduler
from django.utils import timezone
from datetime import timedelta
from news.models import Post, Category
from django.core.mail import send_mail


def my_job():
    last_week = timezone.now() - timedelta(days=7)
    posts = Post.objects.filter(created__gte=last_week)

    for category in Category.objects.all():
        subscribers = category.subscribers.all()
        category_posts = posts.filter(category=category)

        if category_posts.exists():
            for user in subscribers:
                if user.email:
                    send_mail(
                        subject='Статьи за неделю',
                        message='\n'.join([post.title for post in category_posts]),
                        from_email='your_email@gmail.com',
                        recipient_list=[user.email],
                    )


class Command(BaseCommand):
    help = "Запуск планировщика"

    def handle(self, *args, **options):
        scheduler = BlockingScheduler()
        scheduler.add_job(my_job, 'interval', weeks=1)
        scheduler.start()