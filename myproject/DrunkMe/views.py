from django.shortcuts import render, redirect
from DrunkMe.models import User, Bar , Menu , Review , Event
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required  # <--
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm  # <--
from django.contrib.auth import update_session_auth_hash  # <--
from django.contrib import messages  # <--
from social_django.models import UserSocialAuth  # <--

def home(request):
	event_list = Event.objects.all()
	bar_list = Bar.objects.all()

	query = request.GET.get("q")
	if query:
		bar_list = bar_list.filter(Q(name__icontains=query))
		event_list = event_list.filter(Q(name__icontains=query))
	return render(request, 'home.html' , {'event' : event_list , 'bar' : bar_list})

def event(request , num = '1'):
	event = Event.objects.get(id=num)
	return render(request, 'event.html' , {'event' : event})

def detail(request , num = '1'):
	detail = Bar.objects.get(id=num)
	review = Review.objects.all()
	return render(request, 'detail.html' , {'detail' : detail , 'review' : review})

def menu(request , num = '1'):
	barname = Bar.objects.get(id = num)
	menu = Menu.objects.filter(bar = barname)
	return render(request, 'menu.html' , {'menu' : menu , 'barname' : barname})

def search(request):
	menu_list = Menu.objects.all()
	query = request.GET.get("type")
	if query:
		menu_list = menu_list.filter(Q(name__icontains=query))
		
	return render(request, 'search.html' , { 'menu' : menu_list})

def nearby(request):
	return render(request, 'nearby.html')

