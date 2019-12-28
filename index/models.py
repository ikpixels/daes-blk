from django.db import models

class subscribe(models.Model):
	email = models.EmailField()

	def __str__(self):
		return self.email


class Contact(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	email = models.EmailField()
	message = models.TextField()
	updated_at     = models.DateTimeField(auto_now=True,null=True,blank=True)

	def __str__(self):
		return self.name