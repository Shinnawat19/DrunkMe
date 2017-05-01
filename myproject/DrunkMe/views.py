from django.shortcuts import render, redirect
from DrunkMe.models import User, Bar , Menu , Review , Event
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required  # <--
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm  # <--
from django.contrib.auth import update_session_auth_hash  # <--
from django.contrib import messages  # <--
from social_django.models import UserSocialAuth  # <--


def home(request):
	event_list = Event.objects.all()
	bar_list = Bar.objects.all()
	return render(request, 'home.html' , {'event' : event_list , 'bar' : bar_list})

def event(request , num = '1'):
	event = Event.objects.get(id=num)
	return render(request, 'event.html' , {'event' : event})

def detail(request , num = '1'):
	detail = Bar.objects.get(id=num)
	return render(request, 'detail.html' , {'detail' : detail})

def menu(request , num = '1'):
	barname = Bar.objects.get(id = num)
	menu = Menu.objects.filter(bar = barname)

	return render(request, 'menu.html' , {'menu' : menu , 'barname' : barname})

def nearby(request):
	return render(request, 'nearby.html')


def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'settings.html', {
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })
