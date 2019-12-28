from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . models import videos,cordination
from . forms import VideoForm,ASPForm
from account.models import partners

def Videos(request,args=None):

	context = {}
	context['search'] = "Search videos"
	context['partners'] = partners.objects.all().order_by('-id')

	if args:
	 item = videos.objects.filter(category=args,location=args)
	 context['title'] = args
	else:
		item = videos.objects.all()
		context['title'] = "Videos"

	query =request.GET.get('q')

	if query:
		item = item.filter(Q(title__icontains=query)|
		                   Q(category__icontains=query)|
			               Q(location__icontains=query)).distinct()


	page = request.GET.get('page', 1)
	paginator = Paginator(item,12)

	try:
		item = paginator.page(page)
	except PageNotAnInteger:
		item = paginator.page(1)
	except EmptyPage:
		item = paginator.page(paginator.num_pages)

	context['item'] = item

	item2 = videos.objects.all().last()
	context['item2'] = item2


	return render(request,'publications/videos.html',context)


@login_required(login_url="account:account")
def videoform(request):

	context = {}

	context['title'] = "Add youtube extension video link"

	if request.method == "POST":
		form = VideoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('publications:videos')
	else:
		form = VideoForm()
	context['form'] = form

	return render(request,"event/form.html",context)

@login_required(login_url="account:account")
def aspForm(request,id):

	context = {}
	cord = cordination.objects.get(id=id)

	context['title'] = "edit " + str(cord)

	if request.method == "POST":
		form = ASPForm(request.POST,instance=cord)
		if form.is_valid():
			form.save()
			return redirect('account:account')
	else:
		form = ASPForm()
	context['form'] = form
	return render(request,"index/form.html",context)