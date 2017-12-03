from django.db import models
from django.contrib.auth.models import Permission, User

class Main(models.Model):
	""" This is for main/initial page content """
	
	title=models.CharField(max_length=100)
	detail=models.CharField(max_length=200)
	image=models.ImageField(upload_to='image/')
	#Storing the name and time of admin user who has modified/created the main page topic
	username=models.CharField(max_length=100,null=True)
	time=models.DateTimeField(null=True)

class Content(models.Model):
	""" This is for content under the selected topic of main page """	
	main_title=models.CharField(max_length=100)
	title=models.CharField(max_length=200)
	image=models.ImageField()
	detail=models.TextField()
	username=models.CharField(max_length=100,null=True)
	time=models.DateTimeField(null=True)	

class Issue(models.Model):
	""" This is for storing issue faced on anyday """
	date=models.CharField(max_length=100)
	detail=models.CharField(max_length=200)
	rectify=models.CharField(max_length=50)
