from django.shortcuts import render
from .models import Main, Content
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
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
	return render(request, 'helpdoc/index.html',{'main':main,'issue':issue})	

def detail(request,name):
	"""Detail page within content on index headline """
	content=Content.objects.filter(main_title=name)
	return render(request, 'helpdoc/detail.html',{'name':name,'content':content})

@login_required(login_url='/admin_user/')
def creapost(request,name):
	""" Create new post in detail of any index headline """
	if request.method == "POST":
		form = ContentForm(request.POST,request.FILES)
		if form.is_valid():
			title = form.cleaned_data['title']
			detail = form.cleaned_data['detail']
			image = request.FILES['image']
			store=Content(title=title,detail=detail,image=image,main_title=name,report=0)
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

@login_required(login_url='/admin_user/')
def issue(request):
	""" Showing the list of issue faced on specific date  """
	if request.method == "POST":
		tag=request.POST['tag']
		tag2=request.POST['tag2']
		tag3=request.POST['tag3']
		date=request.POST['date1']
		date1=request.POST['date2']
		#Too many conditions are coming as per feedback
		if tag!="All" and tag2 == "All":
			if tag3 == "All":
				issue=Issue.objects.filter(tag=tag).order_by('-date')
				if date:	
					issue=Issue.objects.filter(tag=tag,date__range=[date,datetime.date.today()]).order_by('date')
				if date and date1:	
					issue=Issue.objects.filter(tag=tag,date__range=[date,date1]).order_by('date')
			else:
				issue=Issue.objects.filter(tag=tag,tag3=tag3).order_by('-date')
				if date:	
					issue=Issue.objects.filter(tag=tag,tag3=tag3,date__range=[date,datetime.date.today()]).order_by('date')
				if date and date1:	
					issue=Issue.objects.filter(tag=tag,tag3=tag3,date__range=[date,date1]).order_by('date')								

		else:
			if tag!= "All" and tag2!= "All":
				if tag3 == "All":
					issue=Issue.objects.filter(tag=tag,tag2=tag2).order_by('-date')		
					if date:	
						issue=Issue.objects.filter(tag=tag,tag2=tag2,date__range=[date,datetime.date.today()]).order_by('date')
					if date and date1:	
						issue=Issue.objects.filter(tag=tag,tag2=tag2,date__range=[date,date1]).order_by('date')		

				if tag3!= "All":
					issue=Issue.objects.filter(tag=tag,tag2=tag2,tag3=tag3).order_by('-date')
					if date:	
						issue=Issue.objects.filter(tag=tag,tag2=tag2,tag3=tag3,date__range=[date,datetime.date.today()]).order_by('date')
					if date and date1:	
						issue=Issue.objects.filter(tag=tag,tag2=tag2,tag3=tag3,date__range=[date,date1]).order_by('date')
			else:
				issue=Issue.objects.order_by('-date')
				if date:
					issue=Issue.objects.filter(date__range=[date,datetime.date.today()]).order_by('date')
				if date and date1:
					issue=Issue.objects.filter(date__range=[date,date1]).order_by('date')
									
	else:	
		issue=Issue.objects.order_by('-date')
		#This is done for pre-filling the form with previous entered value
		tag,tag2,tag3,date,date1=('' for i in range(5))

	return render(request,'helpdoc/issue.html',{'issue':issue,'tag':tag,'tag3':tag3,'tag2':tag2,'date':date,'date1':date1})

@login_required(login_url='/admin_user/')
def creaissue(request):
	""" Creating log on issue faced on specific date that have effected client """
	if request.method == "POST":
		form = IssueForm(request.POST)
		if form.is_valid():
			date = form.cleaned_data['date']
			rectify = form.cleaned_data['rectify']
			detail = form.cleaned_data['detail']
			tag = form.cleaned_data['tag']
			tag2 = form.cleaned_data['tag2']
			tag3 = form.cleaned_data['tag3']
			critical = form.cleaned_data['critical']
			effected = form.cleaned_data['effected']
			resolution = form.cleaned_data['resolution']
			store=Issue(date=date,detail=detail,rectify=rectify,tag=tag,resolution=resolution,effected=effected,tag2=tag2,tag3=tag3,critical=critical)
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
                return render(request, 'helpdoc/login.html',{'error_message': 'Please check entered username and password'})   

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
def logout_user(request):
	logout(request)
	return render(request, 'helpdoc/login.html')


def pi_index(request):
	issue=Issue.objects.all().last()
	return render(request,'helpdoc/pi_index.html',{'issue':issue})

def report_category(request):
    if request.method == 'GET':
        cat_id = request.GET['category_id']

    if cat_id:
        cat = Content.objects.get(id=cat_id)
        if cat:
            report = cat.report + 1
            cat.report =  report
            cat.save()

    return HttpResponse(report)

def jsondata(request):
	""" Sending the JSON data for Ajax call """
	data={
	'Q':'All,T1 Holdings/avg,T2 Holdings/avg,Position avg,Settlement Holiday,Others',
	'kite':'All,Holdings,Login,Market watch,Orders,Positions,Charts,Holdings/Orders/Positions,Orders/Positions',
	'Pi':'All,Holdings,Login,Market watch,Orders,Positions,Charts',
	'Nest':'All,Holdings,login,Orders,Positions',
	'Main':'All,Holdings,Orders,Positions',
	'All':'All'
	}
	return JsonResponse(data)    				                     			