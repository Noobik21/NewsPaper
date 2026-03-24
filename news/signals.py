from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post

@receiver(post_save, sender = User)
def add_user_to_common(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name = 'common')
        instance.groups.add(group)


@receiver(post_save, sender=User)
def welcome_user(sender, instance, created, **kwargs):
    if created:
        if instance.email:
            send_mail(
                subject='Добро пожаловать',
                message='Спасибо за регистрацию',
                from_email='your_email@gmail.com',
                recipient_list=[instance.email],

            )

@receiver(post_save, sender=Post)
def notify_subscribers(sender, instance, created, **kwargs):
    if created:
        categories = instance.category.all()
        for category in categories:
            for user in category.subscribes.all():
                if user.email:
                    send_mail(
                        subject=instance.title,
                        message=instance.text[:50],
                        from_email='your_email@gmail.com',
                        recipient_list=[user.email],
                    )