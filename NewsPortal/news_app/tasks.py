from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import datetime

from .models import Post, Category

@shared_task
def send_notifications(preview, pk, title, subscribers):
	html_content = render_to_string(
		'post_created_email.html',
		{
			'text': preview,
			'link': f'{settings.SITE_URL}/news/{pk}',
		}
	)

	msg = EmailMultiAlternatives(
		subject=title,
		body='',
		from_email=settings.DEFAULT_FROM_EMAIL,
		to=subscribers,
	)

	msg.attach_alternative(html_content, 'text/html')
	msg.send()
	print('AddNewPost notify message send')

@shared_task
def notify_subscribers_about_weekly_news():
	#  Your job processing logic here...
	today = datetime.datetime.now()
	last_week = today  - datetime.timedelta(days=7)
	posts = Post.objects.filter(postTime__gte=last_week)
	categories = set(posts.values_list('category__categoryName', flat=True))
	subscribers = set(Category.objects.filter(categoryName__in=categories).values_list('subscribers__email', flat=True))
	html_content = render_to_string(
		'daily_posts.html',
		{
			'link': settings.SITE_URL,
			'posts': posts,
		}
	)

	msg = EmailMultiAlternatives(
		subject='Статьи за неделю',
		body='',
		from_email=settings.DEFAULT_FROM_EMAIL,
		to=subscribers,
	)
	msg.attach_alternative(html_content, 'text/html')
	msg.send()
	print('Weekly notify message send')
