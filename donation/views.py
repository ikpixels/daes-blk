from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from index.snipt import secret_code
from.models import DAESS_Donation


def donation_fuc(request,item,context):
	if request.session.has_key('q'):
		quer = request.session['q']
		item = item.filter(Q(name__icontains=quer)| 
			               Q(phone__icontains=quer)|
			               Q(email__icontains=quer)|
			               Q(ref__icontains=quer)).distinct()
		del request.session['q']

	query =request.GET.get('q')
	if query:
		item =item.filter(Q(name__icontains=query)|
		                  Q(phone__icontains=query)|
		                  Q(email__icontains=query)| 
			              Q(ref__icontains=query)).distinct()


	page = request.GET.get('page', 1)
	paginator = Paginator(item,20)

	try:
		item = paginator.page(page)
	except PageNotAnInteger:
		item = paginator.page(1)
	except EmptyPage:
		item = paginator.page(paginator.num_pages)

	context['give'] = item

def donation(request):

	context = {}
	context['title']="Donate"

	if request.is_ajax():
		Email = request.GET.get('email')
		Name= request.GET.get('dzina')
		Amount= request.GET.get('amount')

		give = DAESS_Donation(name=Name,email=Email,amount=Amount,ref=secret_code())
		give.save()

		request.session['email'] = Email

		host = request.get_host()
		paypal_dict ={'business': settings.PAYPAL_RECEIVER_EMAIL,
                      'amount':Amount,
                      'item_name': 'donation',
                      'invoice':secret_code(),
                      'currency_code': 'USD',
                      'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
                      'return_url': 'http://{}{}'.format(host, reverse('give:donation_thax')),
                      'cancel_return': 'http://{}{}'.format(host, reverse('give:donation')),}
		paypal_form= PayPalPaymentsForm(initial=paypal_dict,button_type="donate")


		

		context['paypal_form'] = paypal_form
		context['name'] = Name
		context['amount'] = Amount

		html = render_to_string('donation/paypal_btn.html',context,request=request)
		return JsonResponse({'data':html})

	return render(request,"donation/give.html",context)

def mpamba(request):
	context = {}

	if request.is_ajax():
		html = render_to_string('donation/mpamba.html',context,request=request)
		return JsonResponse({'data':html})

def mpamba2(request):
	if request.method =='GET':

		Email = request.GET.get('email')
		Name= request.GET.get('dzina')
		Amount= request.GET.get('amount')
		Ref = request.GET.get('ref')
		Phone = request.GET.get('phone')

		give = DAESS_Donation(name=Name,phone=Phone,paypal=False,email=Email,amount=Amount,ref=Ref)
		give.save()

		request.session['email'] = Email

		return redirect('give:donation_thax2')



def airtelmoney(request):
	context = {}

	if request.is_ajax():
		html = render_to_string('donation/airtelmoney.html',context,request=request)
		return JsonResponse({'data':html})


def airtelmoney2(request):
	if request.method =='GET':
		
		Email = request.GET.get('email')
		Name= request.GET.get('dzina')
		Amount= request.GET.get('amount')
		Ref = request.GET.get('ref')
		Phone = request.GET.get('phone')

		give = DAESS_Donation(name=Name,phone=Phone,paypal=False,email=Email,amount=Amount,ref=Ref)
		give.save()

		request.session['email'] = Email

		return redirect('give:donation_thax2')


def donation_thax(request):
	context = {}

	if request.session.has_key('email'):
		Email = request.session['email']


		give = DAESS_Donation.objects.filter(email=Email).last()
		give.verified = True
		give.save()

		context['donar'] = give
		
		del request.session['email']

	return render(request,"donation/thax.html",context)

def donation_thax2(request):
	context = {}

	if request.session.has_key('email'):
		Email = request.session['email']


		give = DAESS_Donation.objects.filter(email=Email).last()
		give.save()

		context['donar'] = give
		
	return render(request,"donation/thax2.html",context)

@login_required(login_url="account:account")
def donation_view(request):
	context = {}

	context['search'] = "Search donar"

	item = DAESS_Donation.objects.all().order_by('-id')
	donation_fuc(request,item,context)

	if request.is_ajax():
		id = request.GET.get('id');

		item2 = DAESS_Donation.objects.get(id=id)
		item2.verified = True
		item2.save()

		item = DAESS_Donation.objects.all().order_by('-id')
		donation_fuc(request,item,context)
		
		html = render_to_string('donation/donation_view2.html',context,request=request)
		return JsonResponse({'data':html})

	return render(request,"donation/donation_view.html",context)