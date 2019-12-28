from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from ckeditor.fields import RichTextField
ASP=(
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
class events(models.Model):
	title    = models.CharField(max_length=200)
	asp      = models.CharField(max_length=200,choices=ASP,blank=True)
	location = models.CharField(max_length=200)
	Event_date  = models.DateField()
	time        = models.TimeField()
	view       = models.PositiveIntegerField(default=0)
	body        = RichTextField()
	image       = models.ImageField(upload_to='events',blank=True,)
	slug        = models.SlugField(unique=True,null=True)
	date        = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('event:event_detail',kwargs ={'slug':self.slug})


def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = events.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_receiver,sender=events)


class item_statistic(models.Model):#recommedation model
    item = models.ForeignKey(events,on_delete=models.CASCADE,related_name="daess_item")
    ip_address = models.CharField(blank=True,max_length=1000)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "views"

@receiver(post_save,sender=item_statistic)
def add_to_statistic(sender,created,instance,**kwargs):
    if created:
        instance.item.view += 1
        instance.item.save()

class documents(models.Model):
	title = models.CharField(max_length=1000)
	docu  = models.FileField(upload_to='Files')
	date  = models.DateTimeField(auto_now_add=True)

	def __str__ (self):
		return self.title

