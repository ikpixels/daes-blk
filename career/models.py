from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from ckeditor.fields import RichTextField
from index.snipt import get_date,create_slug
from django.utils import timezone
import datetime


'''class PostManager(models.Manager):
	def get_query_set(self):
		now = datetime.datetime.now().date()
		return super(PostManager, self).get_query_set().filter(closing_date=now)'''

class job(models.Model):
	CATEGORY = (
		  ('Commission Based','Commission Based'),
		  ('Consultancy','Consultancy'),
		  ('Contract','Contract'),
		  ('Event','Event'),
		  ('Full Time','Full Time'),
		  ('Funding','Funding'),
		  ('Hourly Paid','Hourly Paid'),
		  ('International','International'),
		  ('Internship','Internship'),
		  ('Part Time','Part Time'),
		  ('Scholarship','Scholarship'),
		  ('Seasonal','Seasonal'),
		  ('Short-Term','Short-Term'),
		  ('Temporary','Temporary'),
		  ('Training','Training'),
		  ('Volunteer','Volunteer'),
		)
	user       = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name="job")
	orginisaton = models.CharField(max_length=100,blank=True)
	category = models.CharField(max_length=100,choices=CATEGORY)
	location = models.CharField(max_length=300)
	title = models.CharField(max_length=300)
	link  = models.URLField(blank=True,null=True)
	closing_date = models.DateField()
	body  = RichTextField()
	view  = models.PositiveIntegerField(default=0)
	slug  = models.SlugField(unique=True,null=True)
	date  = models.DateTimeField(auto_now_add=True)
	file  = models.ImageField(upload_to='logo',blank=True)
	created_at     = models.DateTimeField(auto_now_add=True)
	updated_at     = models.DateTimeField(auto_now=True)
	#CareerJob = PostManager()

	def __str__ (self):
		return self.title


	def whenpublished(self):

		post_date = get_date.post_time(self,self.created_at)
		return post_date

	def get_absolute_url(self):
		return reverse('career:job_detail',kwargs ={'slug':self.slug})


def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = job.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_receiver,sender=job)



class item_statistic(models.Model):#recommedation model
    item = models.ForeignKey(job,on_delete=models.CASCADE,related_name="daess_item")
    ip_address = models.CharField(blank=True,max_length=1000)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "views"

@receiver(post_save,sender=item_statistic)
def add_to_statistic(sender,created,instance,**kwargs):
    if created:
        instance.item.view += 1
        instance.item.save()
