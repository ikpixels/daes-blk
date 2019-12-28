from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from account.models import partners
from. forms import JobForm
from django.utils import timezone
import datetime
from index.snipt import ip_address
from . models import job,item_statistic


def Job_list(request,cat=None):

	context = {}
	context['search'] = "Search job"
	context['partners'] = partners.objects.all()

	if request.session.has_key('alert'):
		msg = request.session['alert']
		context['alert'] = msg 
		del request.session['alert']

	if cat:
		Job = job.objects.filter(category=cat).order_by('-updated_at')
		context['title'] = cat + " job"
	else:
		Job = job.objects.all().order_by('-updated_at')
		context['title'] = "Job list"

	if request.session.has_key('q'):
		quer = request.session['q']
		Job = Job.filter(Q(title__icontains=quer)|
		                 Q(orginisaton__icontains=quer)| 
		                 Q(closing_date__icontains=quer)|
		                 Q(category__icontains=quer)|
			             Q(location__icontains=quer)).distinct()
		del request.session['q']

	query =request.GET.get('q')
	if query:
		Job = Job.filter(Q(title__icontains=query)|
		                 Q(orginisaton__icontains=query)| 
		                 Q(closing_date__icontains=query)|
		                 Q(category__icontains=query)|
			             Q(location__icontains=query)).distinct()

	page = request.GET.get('page', 1)
	paginator = Paginator(Job,24)

	try:
		Job = paginator.page(page)
	except PageNotAnInteger:
		Job = paginator.page(1)
	except EmptyPage:
		Job = paginator.page(paginator.num_pages)

	context['job'] = Job

	return render(request,"career/job.html",context)

def job_detail(request,slug):
	context = {}
	context['title'] = "Job dtails"

	context['search'] = "Search job"

	context['partners'] = partners.objects.all()

	Job = job.objects.get(slug=slug)
	context['job'] = Job

	Job_view = job.objects.all().order_by('-view')[:10]
	context['jobView'] = Job_view

	item_statistic.objects.create(item=Job,ip_address=ip_address(request))

	query =request.GET.get('q')
	if query:
		request.session['q'] = query
		return redirect("career:job")

	return render(request,"career/job_detail.html",context)
	

@login_required(login_url="account:account")
def job_form(request):
	
	context = {}

	context['title'] = "Add job"

	context['search'] = "Search job"

	if request.method == "POST":
		form =JobForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save()
			instance.user = request.user
			instance.save()
			request.session["alert"] = "Job added successefully"
			return redirect('career:job')
	else:
		form = JobForm ()
	context['form'] = form

	return render(request,"index/form.html",context)


@login_required(login_url="account:account")
def EditJob(request,id):
	
	context = {}

	context['title'] = "edit job"

	context['search'] = "Search job"

	Job = job.objects.get(id=id)
	
	if request.method == "POST":
		form =JobForm(request.POST,request.FILES,instance=Job)
		if form.is_valid():
			instance = form.save()
			instance.user = request.user
			instance.save()
			request.session["alert"] = "Job edited successefully"
			return redirect('career:job')
	else:
		form = JobForm ()
	context['form'] = form

	return render(request,"index/form.html",context)



def remove_job(request,id):

	Job = job.objects.get(id=id)
	request.session['alert'] = "Job removed successefully"
	Job.delete()



	return redirect('career:job')
