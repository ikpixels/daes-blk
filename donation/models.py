from django.db import models

class DAESS_Donation(models.Model):
	name = models.CharField(max_length=100)
	email =models.EmailField(blank=True)
	phone = models.CharField(max_length=100,blank=True)
	ref  = models.CharField(max_length=100,blank=True)
	amount = models.PositiveIntegerField(null=True,blank=True)
	verified = models.BooleanField(default=False)
	paypal = models.BooleanField(default=True)
	created_at     = models.DateTimeField(auto_now_add=True,null=True,blank=True)

	def __str__(self):
		return self.name
