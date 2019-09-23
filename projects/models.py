from django.db import models

class Project(models.Model):

	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length=100)
	description = models.TextField()
			