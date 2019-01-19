from django.db import models

# Create your models here.
class Job(models.Model):
	image=models.ImageField(upload_to='images/')
	summary=models.CharField(max_length=250)

	# this is used for jobobject(1) in to summary whatever written in the admin page
	def __str__(self):
		return self.summary