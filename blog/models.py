from django.db import models

# Create your models here.

class Blog(models.Model):
	title=models.CharField(max_length=255)
	pub_date=models.DateTimeField()
	image=models.ImageField(upload_to='images/')
	body=models.TextField()

	# some part of body which is show in frontend
	def summary(self):
		return self.body[:40]

		# onli publidh for date
	def pub_date_only(self):
		return self.pub_date.strftime('%b %e, %y')

		# for chnging blogobject(1) in title
	def __str__(self):
		return self.title