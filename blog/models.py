from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField(max_length=400)
	timestamp= models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title