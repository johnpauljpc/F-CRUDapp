from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
	reg_no = models.SlugField(unique = True)
	name = models.CharField(max_length = 50)
	age = models.CharField(max_length = 50)
	department = models.CharField(max_length = 50)
	faculty = models.CharField(max_length = 50)
	about = models.TextField()
	#picture = models.ImageField()

	def __str__(self):
		return self.name


	def get_absolute_url(self):
		return reverse('detail', kwargs={'reg_no': self.reg_no})