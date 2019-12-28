from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save

class partners(models.Model):
	name = models.CharField(max_length=100)
	link = models.URLField(blank=True)
	file = models.ImageField(upload_to="partners")

	def __str__(self):
		return self.name


class TeamMember(models.Model):
	CORD = (
		  ('DAC','DAC'),
		  ('DAECC','DAECC'),
		  ('DSP','DSP'),
		  ('Msamala ASP','Msamala ASP'),
		  ('Nkaya ASP','Nkaya ASP'),
		  ('Kachenga ASP','Kachenga ASP'),
		  ('Chanthunya ASP','Chanthunya ASP'),
		  ('Kalembo ASP','Kalembo ASP'),
		  ('Amidu ASP','Amidu ASP'),
		  ('Sawali ASP','Sawali ASP'),
		  ('Matola ASP','Matola ASP'),
		  ('Phalula ASP','Phalula ASP'),
		  ('Toleza ASP','Toleza ASP'),
		)
	name = models.CharField(max_length=100)
	cordination = models.CharField(max_length=100,choices=CORD,default='DAECC')
	specify     = models.CharField(max_length=100,blank=True)
	position    = models.CharField(max_length=100,blank=True)
	Orgnisation = models.CharField(max_length=100,blank=True)
	desination  = models.CharField(max_length=100,blank=True)
	phone = models.PositiveIntegerField(default=0,blank=True)
	whatsapp = models.CharField(max_length=100,blank=True)
	description = models.TextField(blank=True)
	email = models.EmailField(blank=True)
	facebook = models.URLField(blank=True)
	linkedin = models.URLField(blank=True)
	slug = models.SlugField(unique=True,null=True,blank=True)
	file = models.ImageField(upload_to="Team")

	def __str__ (self):
		return self.name

	def get_absolute_url(self):
		return reverse('index:tema_detail',kwargs ={'slug':self.slug})


def create_slug(instance,new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = TeamMember.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_receiver,sender=TeamMember)
