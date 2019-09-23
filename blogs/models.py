from django.db import models

class Blog(models.Model):

	title = models.CharField(max_length = 100)
	image = models.ImageField(upload_to='images/')
	body = models.TextField()
	pub_date = models.DateTimeField()

	def summarize_body(self):
		return self.body[:100] + "...."

	def __str__(self):
		return self.title