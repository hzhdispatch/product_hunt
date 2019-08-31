from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Product(models.Model):

	title = models.CharField(default='列：抖音-用短视频记录美好生活', max_length=50)
	intro = models.TextField(default='在这里写APP介绍')
	url = models.CharField(default='HTTP：//', max_length=100)
	icon = models.ImageField(default='default_icon.png',upload_to='images/')
	image = models.ImageField(default='default_image.jpg',upload_to='images/')

	votes = models.IntegerField(default=1)	
	pub_date = models.DateField()
	hunter = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.title
    