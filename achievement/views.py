from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from . forms import achievementForm
from account.models import partners
from . models import achievement,item_statistic
from index.snipt import ip_address



def Achievement(request):
	context = {}

	context['title'] = "Our achievement"

	context['partners'] = partners.objects.all()

	context['search'] = "Search Achievement"


	if request.session.has_key('alert'):
		msg = request.session['alert']
		context['alert'] = msg 
		del request.session['alert']

	item = achievement.objects.all()

	query =request.GET.get('q')
	if query:
		item =item.filter(Q(title__icontains=query)| 
			              Q(chievement__icontains=query)).distinct()

	if request.session.has_key('q'):
		quer = request.session['q']
		item =item.filter(Q(title__icontains=quer)| 
			              Q(chievement__icontains=quer)).distinct()
		del request.session['q']

	page = request.GET.get('page', 1)
	paginator = Paginator(item,12)

	try:
		item = paginator.page(page)
	except PageNotAnInteger:
		item = paginator.page(1)
	except EmptyPage:
		item = paginator.page(paginator.num_pages)

	context['item'] = item

	return render(request,"achievement/achievement.html",context)

def Achievement_detail(request,slug):
	context = {}

	context['title'] = "Achievement detail"

	context['search'] = "Search Achievement"

	item = achievement.objects.get(slug=slug)
	context['item'] = item

	context['partners'] = partners.objects.all()

	item_statistic.objects.create(item=item,ip_address=ip_address(request))

	other_item = achievement.objects.all().order_by('-view')[:10]
	context['other_item'] = other_item

	query =request.GET.get('q')
	if query:
		request.session['q'] = query
		return redirect("achievement:achievement")

	return render(request,"achievement/achievement_detail.html",context)

@login_required(login_url="account:account")
def Achievement_form(request):
	context = {}

	context['title'] = "Add success stories"

	context['search'] = "Search Achievement"

	if request.method == "POST":
		form = achievementForm(request.POST,request.FILES)

		if form.is_valid():
			form.save()
			request.session['alert'] = "Item added successefully"
			return redirect("achievement:achievement")

	else:
		form = achievementForm()
	context['form'] = form

	return render(request,"index/form.html",context)


def EditAchievement(request,id):
	context = {}

	context['title'] = "Add success stories"

	context['search'] = "Search Achievement"


	item = achievement.objects.get(id=id)

	if request.method == "POST":
		form = achievementForm(request.POST,request.FILES,instance=item)

		if form.is_valid():
			form.save()
			request.session['alert'] = "Item added successefully"
			return redirect("achievement:achievement")

	else:
		form = achievementForm()
	context['form'] = form

	return render(request,"index/form.html",context)

def remove_stroy(request,id):
	item = achievement.objects.get(id=id)
	request.session['alert'] = "Removed successefully"
	item.delete()
	return redirect('achievement:achievement')