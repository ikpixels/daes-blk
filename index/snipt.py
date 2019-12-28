from django.utils import timezone
from django.conf import settings


from django.urls import reverse
from django.utils.text import slugify
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
import math
import random 
import string
from datetime import date
import datetime


def ip_address(request):

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')# ip address

	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]

	else:
		ip = request.META.get('REMOTE_ADDR')

	return ip


class get_date:#generating model date
	def post_time(self,post_date):

		now = timezone.now()

		diff= now - post_date

		if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:

			seconds= diff.seconds

			if seconds == 1:
				return str(seconds) +  "second ago"

			else:
				return str(seconds) + " seconds ago"


		if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
			minutes= math.floor(diff.seconds/60)

			if minutes == 1:
				return str(minutes) + " minute ago"

			else:
				return str(minutes) + " minutes ago"


		if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:

			hours= math.floor(diff.seconds/3600)

			if hours == 1:

				return str(hours) + " hour ago"


			else:
				return str(hours) + " hours ago"

        # 1 day to 30 days
		if diff.days >= 1 and diff.days < 30:

			days= diff.days

			if days == 1:

				return str(days) + " day ago"

			else:
				return str(days) + " days ago"

		if diff.days >= 30 and diff.days < 365:
			months= math.floor(diff.days/30)


			if months == 1:
				return str(months) + " month ago"

			else:
				return str(months) + " months ago"

		if diff.days >= 365:

			years= math.floor(diff.days/365)

			if years == 1:
				return str(years) + " year ago"

			else:
				return str(years) + " years ago"


		


def secret_code():#generating secret_code
	date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
	rand_str = "".join([random.choice(string.digits) for count in range (3)])
	return date_str + rand_str


def create_slug(model_name,item,instance,new_slug=None):
    slug = slugify(instance.item)
    if new_slug is not None:
        slug = new_slug
    qs = model_name.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug