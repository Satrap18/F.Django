from django.db import models

# Create your models here.

class Todo(models.Model):
	title = models.CharField(max_length=30)
	body = models.TextField()
	time = models.DateTimeField()



	def __str__(self):
		return self.title