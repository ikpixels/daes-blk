from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,logout, login as dj_login
from . forms import PartinersForm,TeamForm
from . models import TeamMember
from publications.models import cordination

def Login(request):
	context = {}

	context['title'] = "Login"

	if request.method =="POST":
		username = request.POST['name']
		password = request.POST['pass']
		user = authenticate(username=username,password=password)
		if user:
			dj_login(request,user)
			return redirect('account:dashboard')
			
		else:
			context['error']="Provide valide Credientials!!!"
			return redirect('account:account')

	
	return render(request,'account/login_form.html',context)

def Logout(request):
	logout(request)
	return redirect("account:account")


@login_required(login_url="account:account")
def dashboard(request):
	context = {}

	context['title'] = "Dashboard"
	context['cord'] = cordination.objects.all()
	context['search'] = "Search donar"

	query =request.GET.get('q')
	if query:
		request.session['q'] = query
		return redirect("give:donation_view")

	return render(request,'account/dashboard.html',context)

def Partiners(request):

	context = {}

	context['title'] = "Add Partiner"

	if request.method == "POST":
		form = PartinersForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect("index:index")
	else:
		form = PartinersForm()
	context['form'] = form

	return render(request,"index/form.html",context)


@login_required(login_url="account:account")
def teamMember(request):

	context = {}

	context['title'] = "Add Member"

	if request.method == "POST":
		form = TeamForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			request.session['alert'] = "Item added successefully"
			return redirect("index:team")
	else:
		form = TeamForm()
	context['form'] = form

	return render(request,"index/form.html",context)

@login_required(login_url="account:account")
def EditTeam(request,slug):

	context = {}

	context['title'] = "Add Member"

	Team = TeamMember.objects.get(slug=slug)

	if request.method == "POST":
		form = TeamForm(request.POST,request.FILES,instance=Team)
		if form.is_valid():
			form.save()
			request.session['alert'] = "Item added successefully"
			return redirect("index:team")
	else:
		form = TeamForm()
	context['form'] = form

	return render(request,"index/form.html",context)

def removemember(request,id):
	Team = TeamMember.objects.get(id=id)
	request.session['alert'] = "Team member removed siccessefully"
	Team.delete()
	return redirect('index:team')




