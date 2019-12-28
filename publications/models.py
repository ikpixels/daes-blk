from django.db import models
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField

class videos(models.Model):
	CATEGORY = (
		 ('Agricuture Extension video','Agricuture Extension video'),
		 ('Nutrition Extension videos','Nutrition Extension videos'),
		 ('Documentary','Documentary'),
		 ('Success stories','Success stories'),
		 ('Event','Event'),
		)
	LOCATION = (
		  ('Msamala','Msamala'),
		  ('Nkaya','Nkaya'),
		  ('Kachenga','Kachenga'),
		  ('Chanthunya','Chanthunya'),
		  ('Kalembo','Kalembo'),
		  ('Amidu','Amidu'),
		  ('Sawali','Sawali'),
		  ('Matola','Matola'),
		  ('Phalula','Phalula'),
		  ('Toleza','Toleza'),
		)
	title = models.CharField(max_length=100)
	category = models.CharField(max_length=100,default="Extension video",choices=CATEGORY)
	location = models.CharField(max_length=100,blank=True,choices=LOCATION)
	video = models.URLField() 

	def __str__(self):
		return self.title

	def split_link(self):
		link = self.video
		youtube,Id = link.split('?v=')
		final_link = "https://www.youtube.com/embed/" + Id
		return final_link

class cordination(models.Model):
	asp = models.CharField(max_length=100)
	male = models.PositiveIntegerField(null=True,blank=True)
	female = models.PositiveIntegerField(null=True,blank=True)
	total = models.PositiveIntegerField(null=True,blank=True)
	vac_no = models.PositiveIntegerField(null=True,blank=True)
	vac_name = models.CharField(max_length=100,blank=True)
	discription = RichTextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.asp
