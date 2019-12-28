from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . forms import PJForm
from . models import Projects,item_statistic
from account.models import partners
from index.snipt import ip_address




def projects_view(request,args=None):

	context = {}
	context['partners'] = partners.objects.all()

	context['pj_count'] = Projects.objects.all().count()


	if request.session.has_key('alert'):
		msg = request.session['alert']
		context['alert'] = msg 
		del request.session['alert']

	if args:
		item = Projects.objects.filter(area=args,areas=args).order_by('-id')
		context['title'] = args + "|projects"

	else:
		item = Projects.objects.all().order_by('-id')
		context['title'] = "Our projects"

	if request.session.has_key('q'):#session from pj detail
		quer = request.session['q']
		item = item.filter(Q(name__icontains=quer)|
		                     Q(area__icontains=quer)|
		                     Q(areas__icontains=quer)|
			                 Q(NGO__icontains=quer)).distinct()
		del request.session['q']

	query =request.GET.get('q')
	if query:
		item = item.filter(Q(name__icontains=query)|
		                     Q(area__icontains=query)|
		                     Q(areas__icontains=query)|
			                 Q(NGO__icontains=query)).distinct()


	page = request.GET.get('page', 1)
	paginator = Paginator(item,12)

	try:
		item = paginator.page(page)
	except PageNotAnInteger:
		item = paginator.page(1)
	except EmptyPage:
		item = paginator.page(paginator.num_pages)

	context['pj'] = item

	context['search'] = "Search projects"

	return render(request,'projects/projects.html',context)

def PjDetail(request,slug):
	context = {}

	context['title'] = "Project detail"

	context['search'] = "Search projects"
	context['pj_count'] = Projects.objects.all().count()

	context['partners'] = partners.objects.all()

	pj = Projects.objects.get(slug=slug)
	context['pj'] = pj

	item_statistic.objects.create(item=pj,ip_address=ip_address(request))

	pj_d = Projects.objects.all().order_by('-view')[:10]
	context['pj_d'] = pj_d

	query =request.GET.get('q')
	if query:
		request.session['q'] = query
		return redirect("projects:projects")

	return render(request,'projects/projects_detail.html',context)

@login_required(login_url="account:account")
def PjForm(request):

	context = {}

	context['title'] = "Add project"

	context['search'] = "Search projects"

	if request.method == "POST":
		form = PJForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			request.session['alert'] = "Added successefully"
			return redirect('projects:projects')
	else:
		form = PJForm()

	context['form'] = form

	query =request.GET.get('q')
	if query:
		request.session['q'] = query
		return redirect("projects:projects")

	return render(request,"index/form.html",context)

@login_required(login_url="account:account")
def EditPj(request, id):

	context = {}

	context['title'] = "Edit project"

	context['search'] = "Search projects"

	pj = Projects.objects.get(id=id)

	if request.method == "POST":
		form = PJForm(request.POST,request.FILES,instance=pj)
		if form.is_valid():
			form.save()
			request.session['alert'] = "Added successefully"
			return redirect('projects:projects')
	else:
		form = PJForm()

	context['form'] = form

	query =request.GET.get('q')
	if query:
		request.session['q'] = query
		return redirect("projects:projects")

	return render(request,"index/form.html",context)

def removePj(request,id):
	pj = Projects.objects.get(id=id)
	request.session['alert'] = "Removed successefully"
	pj.delete()
	return redirect ("projects:projects")

def pj_document_detail(request,id):

	context = {}

	context['title'] = "Documents detail"

	docu = Projects.objects.get(id=id)
	context['docu'] = docu

	return render(request,"event/document_detail.html",context)

