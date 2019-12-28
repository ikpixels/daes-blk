from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from event.models import events
from achievement.models import achievement
from account.models import partners
from account.models import TeamMember
from . models import subscribe,Contact
from donation.models import DAESS_Donation
from django.core.mail import EmailMultiAlternatives
from publications.models import videos,cordination


def index(request):

	context = {}

	context['title'] = "Balaka DAESS"
	context['event'] = events.objects.all().order_by('-id')[:2]
	context['partners'] = partners.objects.all().order_by('-id')
	context['achievement'] = achievement.objects.all().order_by('-id')[:2]
	context['donar'] = DAESS_Donation.objects.all().last()

	query =request.GET.get('q')
	if query:
		request.session['q'] = query
		return redirect("event:event")

	context['search'] = "Search events"
	
	return render(request,"index/index.html",context)

def about_daess(request):
	context = {}

	context['title'] = "About BLK-DAESS"

	context['partners'] = partners.objects.all()

	context['contacts'] = TeamMember.objects.all()

	query =request.GET.get('q')
	if query:
		request.session['q'] = query
		return redirect("event:event")

	context['search'] = "Search events"

	return render(request,"index/about_daess.html",context)


def daess_objectives(request):
	context = {}

	context['title'] = "Our objectives"

	context['partners'] = partners.objects.all()

	context['contacts'] = TeamMember.objects.all()


	query =request.GET.get('q')
	if query:
		request.session['q'] = query
		return redirect("event:event")

	context['search'] = "Search events"

	return render(request,"index/daess_objectives.html",context)


def daess_structure(request):
	context = {}

	context['title'] = "Our structure"

	context['partners'] = partners.objects.all()

	context['contacts'] = TeamMember.objects.all()

	query =request.GET.get('q')

	if query:
		request.session['q'] = query
		return redirect("event:event")

	context['search'] = "Search events"

	return render(request,"index/daess_structure.html",context)

def tema_detail(request,slug):
	context = {}



	t_member = TeamMember.objects.get(slug=slug)
	context['team'] = t_member

	context['contacts'] = TeamMember.objects.all()

	context['title'] = t_member
	context['partners'] = partners.objects.all()

	return render(request,"index/team_detail.html",context)

def contact(request):
	 context = {}

	 context['title'] = "Contacts"

	 context['partners'] = partners.objects.all()

	 context['contacts'] = TeamMember.objects.all()

	 query =request.GET.get('q')

	 if query:
	 	request.session['q'] = query
	 	return redirect("event:event")

	 if request.is_ajax():

	 	name = request.GET.get('name')
	 	phone = request.GET.get('phone')
	 	email = request.GET.get('email')
	 	message = request.GET.get('message')



	 	contact = Contact(name=name,email=email,phone=phone,message=message)
	 	contact.save()

	 	html = render_to_string('index/contact2.html',context,request=request)
	 	return JsonResponse({'data':html})

	 context['search'] = "Search events"

	 return render(request,"index/contact.html",context)


def team(request,args=None):
	 context = {}

	 
	 context['search'] = "Team member"
	 context['partners'] = partners.objects.all()

#_____________________________________________
	 if request.session.has_key('alert'):
	 	msg = request.session['alert']
	 	context['alert'] = msg 
	 	del request.session['alert']

#______________________________________________
	 if args:
	 	contact = TeamMember.objects.filter(cordination=args).order_by('-id')
	 	context['title'] = args + ' team member'
	 	context['team'] = args
	 else:
	 	context['title'] = "Our team"
	 	contact = TeamMember.objects.all().order_by('-id')

#_______________________________________________

	 if request.session.has_key('q'):
	 	quer = request.session['q']
	 	contact = contact.filter(Q(name__icontains=quer)|
		                         Q(cordination__icontains=quer)|
		                         Q(specify__icontains=quer)|
			                     Q(Orgnisation__icontains=quer)).distinct()
	 	del request.session['q']

	 query =request.GET.get('q')

	 if query:
	 	contact = contact.filter(Q(name__icontains=query)|
		                         Q(cordination__icontains=query)|
		                         Q(specify__icontains=query)|
			                     Q(Orgnisation__icontains=query)).distinct()

	 page = request.GET.get('page', 1)
	 paginator = Paginator(contact,12)

	 try:
	 	contact = paginator.page(page)

	 except PageNotAnInteger:
	 	contact = paginator.page(1)
	 except EmptyPage:
	 	contact = paginator.page(paginator.num_pages)

	 context['contact'] = contact

	 return render(request,"index/team.html",context)

def ASP(request,asp):

	context = {}
	context['title'] = str(asp)
	context['title2'] = str(asp)

	name,_ = asp.split()
	context['name'] = name

	try:
		cord = cordination.objects.get(asp=asp)
		context['cord'] = cord
	except cordination.DoesNotExist:
		pass

	team = TeamMember.objects.filter(cordination=asp)
	context['team'] = team

	context['partners'] = partners.objects.all()

	return render(request,"index/asp.html",context)

def Subscribe(request):
	context ={}
	email = request.GET['email']

	try:
		mail = subscribe.objects.filter(email=email)

		if mail:
			info ="false"
		else:
			subs = subscribe(email=email)
			subs.save()
			info ="true"
	except subscribe.DoesNotExist:
		pass
	return JsonResponse({'data':info})
	

def unsubscribe(request):
	context ={}

	email = request.GET['email']

	try:
		mail = subscribe.objects.get(email=email)

		if mail:
			mail.delete()
			info = "true"
		else:
			info ="false"

	except subscribe.DoesNotExist:
		info ="false"
		

	return JsonResponse({'data':info})

