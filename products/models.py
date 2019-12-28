from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from index.snipt import create_slug

class products(models.Model):

	CATEGORIES = (
		('Banana','Banana'),
		('Beans','Beans'),
		('Cereals','Cereals'),
		('Chemicals','Chemicals'),
		('Fruits','Fruits'),
		('Garri','Garri'),
		('Livestock','Livestock'),
		('Melon','Melon'),
		('Oil Nature','Oil Nature'),
		('Pawpaw','Pawpaw'),
		('Plantain','Plantain'),
		('Seeds','Seeds'),
		('Tomatoes','Tomatoes'),
		('Tractors','Tractors'),
		('Tubers','Tubers'),
		('Vegetables','Vegetables'),
		('Yam','Yam'),
		)
	farmer = (
		('Smallholder','Smallholder'),
		('Cooperative','Cooperative'),
		('Agro dealers','Agro dealers'),
		('Others','Others'),)

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

	
	user       = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name="owner")
	category   = models.CharField(max_length=300,choices=CATEGORIES,blank=True)
	item       = models.CharField(max_length=100,null=True,blank=True)
	price      = models.DecimalField(max_digits=18, decimal_places=2,null=True,blank=True)
	new_price  = models.DecimalField(max_digits=18,blank=True,null=True,decimal_places=2)
	price_com  = models.CharField(max_length=30,blank=True)
	location   = models.CharField(max_length=30,choices=LOCATION,default='Matola')
	stock      = models.CharField(max_length=100,blank=True,null=True)
	owner      = models.CharField(max_length=600,choices=farmer,null=True,blank=True)
	specify    = models.CharField(max_length=40,blank=True)
	real_name      = models.CharField(max_length=600,null=True,blank=True)
	phone          = models.PositiveIntegerField(null=True,blank=True)
	whatsapp       = models.CharField(max_length=100,blank=True)
	email          = models.EmailField(blank=True)
	view           = models.PositiveIntegerField(default=0)
	slug           = models.SlugField(unique=True,null=True,blank=True)
	Dicription     = models.TextField(blank=True,null=True)
	file           = models.ImageField(upload_to='Products',null=True,blank=True)
	created_at     = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	updated_at     = models.DateTimeField(auto_now=True,null=True,blank=True)

	def __str__ (self):
		return self.item

	def get_absolute_url(self):
		return reverse('products:product_detail',kwargs ={'slug':self.slug})


def create_slug(instance,new_slug=None):
    slug = slugify(instance.item)
    if new_slug is not None:
        slug = new_slug
    qs = products.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug

def pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_receiver,sender=products)


class item_statistic(models.Model):#recommedation model
    item = models.ForeignKey(products,on_delete=models.CASCADE,related_name="daess_item")
    ip_address = models.CharField(blank=True,max_length=1000)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "views"

@receiver(post_save,sender=item_statistic)
def add_to_statistic(sender,created,instance,**kwargs):
    if created:
        instance.item.view += 1
        instance.item.save()
