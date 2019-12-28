from django.shortcuts import render,redirect
from . forms import ProductForm
from . models import products,item_statistic
from account.models import partners
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from index.snipt import ip_address

def Products(request,args=None):
	
	context = {}

	context['partners'] = partners.objects.all()

	context['item2'] = products.objects.all().last()


	if request.session.has_key('alert'):
		msg = request.session['alert']
		context['alert'] = msg 
		del request.session['alert']

	if args:
		item = products.objects.filter(location=args,category=args).order_by('-updated_at')
		context['title'] = args
	else:
		context['title'] = "Products"
		item = products.objects.all().order_by('-updated_at')

	query =request.GET.get('q')

	if request.session.has_key('q'):
		quer = request.session['q']
		item = item.filter(Q(item__icontains=quer)| 
			               Q(category__icontains=quer)).distinct()
		del request.session['q']

	if query:
		item =item.filter(Q(item__icontains=query)| 
			              Q(category__icontains=query)).distinct()


	page = request.GET.get('page', 1)
	paginator = Paginator(item,12)

	try:
		item = paginator.page(page)
	except PageNotAnInteger:
		item = paginator.page(1)
	except EmptyPage:
		item = paginator.page(paginator.num_pages)

	context['item'] = item

	context['search'] = "Search products"

	return render(request, "products/products.html", context)


@login_required(login_url="account:account")
def products_form(request):
	context = {}

	context['title'] = "Add product"

	context['search'] = "Search products"

	if request.method == "POST":
		form = ProductForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save()
			instance.user = request.user
			instance.save()
			request.session['alert'] = "Item adited successefully"
			return redirect("products:products")
	else:
		form = ProductForm()
	context['form'] = form

	return render(request,"index/form.html",context)

@login_required(login_url="account:account")
def Editproduct(request,slug):
	context = {}

	context['title'] = "Add product"

	context['search'] = "Search products"

	item = products.objects.get(slug=slug)

	if request.method == "POST":
		form = ProductForm(request.POST,request.FILES,instance=item)
		if form.is_valid():
			instance = form.save()
			instance.user = request.user
			instance.save()
			request.session['alert'] = "Item adited successefully"
			return redirect("products:products")
	else:
		form = ProductForm()
	context['form'] = form

	return render(request,"index/form.html",context)

def removeitem(request,id):
	item = products.objects.get(id=id)
	request.session['alert'] = "Item removed successefully"
	item.delete()
	return redirect("products:products")

def product_detail(request,slug):
	context = {}

		
	context['title'] = slug
	context['search'] = "Search products"
	context['item2'] = products.objects.all().last()

	item = products.objects.get(slug=slug)
	context['item'] = item

	item_statistic.objects.create(ip_address=ip_address(request),item=item)

	item2 = products.objects.all()
	item3= item2.filter(Q(item=item.item)| 
			            Q(category=item.category)).distinct()
	context['related'] = item3

	query =request.GET.get('q')
	if query:
		request.session['q'] = query
		return redirect("products:products")

	context['partners'] = partners.objects.all()
	return render(request, "products/products_detail.html", context)