from django.shortcuts import render
from .models import Main, Content
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ContentForm, MainForm,IssueForm,UserForm
from .models import Main, Content,Issue
import datetime

@login_required(login_url='/admin_user/')
def post(request):
	""" This posts the content on main page """
	if request.method == "POST":
		form = MainForm(request.POST,request.FILES)
		if form.is_valid():
			title = form.cleaned_data['title']
			detail = form.cleaned_data['detail']
			image = request.FILES['image']
			store=Main(title=title,detail=detail,image=image)
			store.save()
			return redirect('https://helpdoc.herokuapp.com/index/') 
	else:
		form =MainForm()		

	return render(request, 'helpdoc/post.html', {'form': form})	            	

def index(request):
	"""This is the main landing page, shows all the main content stored """
	main=Main.objects.all()
	issue=Issue.objects.all().last()
	if request.user:
		admin="yes"
	return render(request, 'helpdoc/index.html',{'main':main,'issue':issue,'admin':admin})	

def detail(request,name):
	"""Detail page within content on index headline """
	content=Content.objects.filter(main_title=name)
	if request.user:
		admin="yes"
	return render(request, 'helpdoc/detail.html',{'name':name,'content':content,'admin':admin})

@login_required(login_url='/admin_user/')
def creapost(request,name):
	""" Create new post in detail of any index headline """
	if request.method == "POST":
		form = ContentForm(request.POST,request.FILES)
		if form.is_valid():
			title = form.cleaned_data['title']
			detail = form.cleaned_data['detail']
			image = request.FILES['image']
			store=Content(title=title,detail=detail,image=image,main_title=name)
			store.save()
			return redirect('https://helpdoc.herokuapp.com/index/')
	else:
		form =ContentForm()		

	return render(request, 'helpdoc/creapost.html', {'form': form,'name':name})	

@login_required(login_url='/admin_user/')
def editmain(request,id):
	""" Edit headline content """
	data=Main.objects.filter(id=id).first()
	if request.method == "POST":
		form = MainForm(request.POST,request.FILES)
		if form.is_valid():
			title = form.cleaned_data['title']
			detail = form.cleaned_data['detail']
			image = request.FILES['image']
			data.title=title
			data.detail=detail
			data.image=image
			data.save()
			
			return redirect('https://helpdoc.herokuapp.com/index/') 
	else:
		form =MainForm()	

	return render(request, 'helpdoc/editmain.html', {'form': form,'data':data,'id':id})

@login_required(login_url='/admin_user/')
def editdetail(request,id):
	""" Edit content of detail subject under index headline """
	data=Content.objects.filter(id=id).first()
	if request.method == "POST":
		form = ContentForm(request.POST,request.FILES)
		if form.is_valid():
			title = form.cleaned_data['title']
			detail = form.cleaned_data['detail']
			image = request.FILES['image']
			data.title=title
			data.detail=detail
			data.image=image
			data.save()
			
			return redirect('https://helpdoc.herokuapp.com/index/') 
	else:
		form =ContentForm()	

	return render(request, 'helpdoc/editdetail.html', {'form': form,'data':data,'id':id})	

def issue(request):
	""" Showing the list of issue faced on specific date that have effected client """
	issue=Issue.objects.all()
	return render(request,'helpdoc/issue.html',{'issue':issue,})

@login_required(login_url='/admin_user/')
def creaissue(request):
	""" Creating log on issue faced on specific date that have effected client """
	if request.method == "POST":
		form = IssueForm(request.POST)
		if form.is_valid():
			date = form.cleaned_data['date']
			rectify = form.cleaned_data['rectify']
			detail = form.cleaned_data['detail']
			store=Issue(date=date,detail=detail,rectify=rectify)
			store.save()
			return redirect('https://helpdoc.herokuapp.com/issue/') 
	else:
		form =IssueForm()		

	return render(request, 'helpdoc/creaissue.html', {'form': form})

def admin_user(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)        
            if user is not None:
                login(request, user)  
                return redirect('https://helpdoc.herokuapp.com/index/')

            else:    
                return render(request, 'helpdoc/login.html',{'error_message': 'Please check your username and password'})   

        else:   
            return render(request, 'helpdoc/login.html')

def admin_register(request):
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return render(request, 'helpdoc/login.html')
        context = {
            "form": form,
        }
        return render(request, 'helpdoc/admin_reg.html',{'form': form,} )

@login_required(login_url='/admin_user/')
def logout(request):
	return render(request, 'helpdoc/login.html')


def pi_index(request):
	issue=Issue.objects.all().last()
	return render(request,'helpdoc/pi_index.html',{'issue':issue})	                     			