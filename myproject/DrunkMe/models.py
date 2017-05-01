from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	userID = models.CharField(null=True , max_length=50)
	userPassword = models.CharField(null=True , max_length=50)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50 , blank=True)
	address = models.CharField(max_length=100 , blank=True)
	phone = models.CharField(max_length=50 , blank=True)
	point = models.IntegerField(default = 0)
	image = models.ImageField(upload_to='images/user' , blank=True)
	def __unicode__(self):
		return "%s"%(self.name)

class Bar(models.Model):
	name = models.CharField(max_length=50 , editable = True)
	content = models.CharField(max_length=500)
	address = models.CharField(max_length=100)
	rating = models.IntegerField(default = 0)
	phone = models.CharField(max_length=50 , blank=True)
	logo = models.ImageField(upload_to='images/bar' , blank=True)
	image1 = models.ImageField(upload_to='images/bar' , blank=True)
	image2 = models.ImageField(upload_to='images/bar' , blank=True)
	image3 = models.ImageField(upload_to='images/bar' , blank=True)
	image4 = models.ImageField(upload_to='images/bar' , blank=True)
	image5 = models.ImageField(upload_to='images/bar' , blank=True)
	status = models.CharField(max_length=50 , default = 'open')
	promotion = models.CharField(max_length=100 , blank=True)
	happyhours = models.CharField(max_length=100 , blank=True)
	def __unicode__(self):
		return "%s"%(self.name)

class Menu(models.Model):
	bar = models.ForeignKey(Bar , on_delete = models.CASCADE)
	name = models.CharField(max_length=50 , null=False)
	price = models.DecimalField(max_digits = 15 , decimal_places = 2 , null = False)

class Review(models.Model):
	bar = models.ForeignKey(Bar , on_delete = models.CASCADE)
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	comment = models.CharField(max_length=100)
	rating = models.IntegerField(default = 0)
	date = models.DateTimeField(auto_now_add = True)

class Event(models.Model):
	image = models.ImageField(upload_to='images/event')
	name = models.CharField(max_length=50)
	content = models.CharField(max_length=500)
	location = models.CharField(max_length=100)
	ticket = models.CharField(max_length=50 , default = 'free')
	date = models.DateTimeField()
	phone = models.CharField(max_length=50)