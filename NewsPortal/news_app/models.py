from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
	ratingAuthor = models.SmallIntegerField(default=0)
	authorUser = models.OneToOneField(User, on_delete=models.CASCADE)

	def update_rating(self):
		postRat = self.post_set.aggregate(postRating=Sum('rating'))
		pRat = 0
		pRat += postRat.get('postRating')
		commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
		cRat = 0
		cRat += commentRat.get('commentRating')
		self.ratingAuthor = pRat * 3 + cRat
		self.save()

	def __str__(self):
		return self.authorUser.username

class Category(models.Model):
	categoryName = models.CharField(max_length=64, unique=True)
	subscribers = models.ManyToManyField(User, related_name='categories')

	def __str__(self):
		return self.categoryName


class Post(models.Model):
	NEWS = 'NW'
	ARTICLE = 'AR'
	POST_TYPE = (
		(NEWS, 'Новость'),
		(ARTICLE, 'Статья')
	)
	categoryType = models.CharField(max_length=2, choices=POST_TYPE, default=ARTICLE)
	postTime = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=128)
	content = models.TextField()
	rating = models.SmallIntegerField(default=0)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	category = models.ManyToManyField(Category, through='PostCategory')

	def like(self):
		self.rating += 1
		self.save()

	def dislike(self):
		self.rating -= 1
		self.save()

	def preview(self):
		return '{}...'.format(self.content[:123])

	def __str__(self):
		return f'{self.title.title()}: {self.content}. Автор: {self.author}, категория: {self.category}, рейтинг: {self.rating}'

	def get_absolute_url(self):
		return f'/news/{self.id}'

class PostCategory(models.Model):
	postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
	categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

#	def __str__(self):
#		return f' {self.post.title} | {self.category.categoryName}'


class Comment(models.Model):
	comment = models.TextField()
	commentTime = models.DateTimeField(auto_now_add=True)
	rating = models.SmallIntegerField(default=0)
	commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
	commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)

	def like(self):
		self.rating += 1
		self.save()

	def dislike(self):
		self.rating -= 1
		self.save()

	def __str__(self):
		return self.comment
