from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from account.models import partners
from django.http import HttpResponseRedirect
from . models import events,documents,item_statistic
from . forms import eventForm,DocumentForm
from index.snipt import ip_address

def event(request, asp=None):

	context = {}
	context['partners'] = partners.objects.all()
	context['search'] = "Search upcoming events"

	if request.session.has_key('alert'):
		msg = request.session['alert']
		context['alert'] = msg 
		del request.session['alert']

	if asp:
		Event = events.objects.filter(asp=asp).order_by('-id')
		context['title'] = asp + " upcoming event"
	else:
		Event = events.objects.all().order_by('-id')
		context['title'] = "Upcoming event"

	query =request.GET.get('q')
	if query:
		Event = Event.filter(Q(title__icontains=query)|
		                     Q(Event_date__icontains=query)| 
			                 Q(location__icontains=query)).distinct()

	if request.session.has_key('q'):
		quer = request.session['q']
		Event = Event.filter(Q(title__icontains=quer)|
		                     Q(Event_date__icontains=quer)| 
			                 Q(location__icontains=quer)).distinct()
		
		del request.session['q']

	


	page = request.GET.get('page', 1)
	paginator = Paginator(Event,12)

	try:
		Event = paginator.page(page)
	except PageNotAnInteger:
		Event = paginator.page(1)
	except EmptyPage:
		Event = paginator.page(paginator.num_pages)

	context['event'] = Event

	return render(request,"event/event.html",context)

def event_detail(request,slug):
	context = {}

	context['title'] = "Event detail"

	context['partners'] = partners.objects.all()

	context['search'] = "Search upcoming events"

	Event = events.objects.get(slug=slug)
	context['event'] = Event

	item_statistic.objects.create(item=Event,ip_address=ip_address(request))

	Other_Event = events.objects.all()[:10]
	context['Other_Event'] = Other_Event

	query =request.GET.get('q')
	if query:
		request.session['q'] = query
		return redirect("event:event")

	return render(request,"event/event_detail.html",context)


@login_required(login_url="account:account")
def event_form(request):
	context = {}

	context['title'] = "Create event"

	context['search'] = "Search upcoming events"

	if request.method == "POST":
		form = eventForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			request.session['alert'] = "Event added successefuly"
			return redirect("event:event")
	else:
		form = eventForm()
	context['form'] = form

	return render(request,"index/form.html",context)


@login_required(login_url="account:account")
def Editevent(request,id):
	context = {}

	context['title'] = "Create event"

	context['search'] = "Search upcoming events"

	Event = events.objects.get(id=id)

	if request.method == "POST":
		form = eventForm(request.POST,request.FILES,instance=Event)
		if form.is_valid():
			form.save()
			request.session['alert'] = "Event added successefuly"
			return redirect("event:event")
	else:
		form = eventForm()
	context['form'] = form

	return render(request,"index/form.html",context)

def RemoveEvent(request,id):
	Event = events.objects.get(id=id)
	request.session["alert"] = "Removed successefuly"
	Event.delete()
	return redirect("event:event")



@login_required(login_url="account:account")
def DocuForm(request):
	context = {}

	context['title'] = "Add document"

	if request.method == "POST":
		form = DocumentForm(request.POST,request.FILES)

		if form.is_valid():
			form.save()
			return redirect('index:index')

	else:
		form = DocumentForm()
	context['form'] = form

	return render(request,"event/form.html",context)


def document_view(request):

	context = {}

	context['title'] = "Documents"

	context['search'] = "Search documents"

	docu = documents.objects.all()

	query =request.GET.get('q')

	if query:
		docu = docu.filter(Q(title__icontains=query)|
			               Q(date__icontains=query)).distinct()


	page = request.GET.get('page', 1)
	paginator = Paginator(docu,24)

	try:
		docu = paginator.page(page)
	except PageNotAnInteger:
		docu = paginator.page(1)
	except EmptyPage:
		docu = paginator.page(paginator.num_pages)

	context['docu'] = docu

	return render(request,"event/documents.html",context)


def document_detail(request,id):

	context = {}

	context['title'] = "Documents detail"

	docu = documents.objects.get(id=id)
	context['docu'] = docu

	return render(request,"event/document_detail.html",context)