from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length =20)
	text = models.CharField(max_length=2000)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.title

class Comments(models.Model):
	blog = models.ForeignKey(Blog)
	comment_text = models.CharField(max_length=100)
	date  = models.DateTimeField('date of comment')
	def __str__(self):
		return self.comment_text
