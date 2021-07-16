from django.shortcuts import render, redirect
from django.db.models import Avg, Max, Min
from .models import Gigs
import time
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User


def get_landing_page(request):
    landing_slider = LandingSlider.objects.all()
    services = Services.objects.all()
    cats = Category.objects.all()

    args = {
            'landing_slider': landing_slider,
            'services': services,
            'cats': cats
        }
    return render(request, 'mainview/landingPage.html', args)


# @login_required(login_url='user_login')
def buying_view(request):
    gigs = Gigs.objects.filter(is_publish=True).order_by('-gig_click_count')

    args = {
        'gigs': gigs
    }
    return render(request, 'buyingview/main.html', args)

# @login_required(login_url='user_login')
def gig_details(request, gig_slug):
    gigs = Gigs.objects.filter(gig_slug=gig_slug).first()



    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    u = DummyUser(user=ip)

    result = DummyUser.objects.filter(Q(user__icontains=ip))

    if len(result) == 1:
        print("It wont Work Dude!")
    elif len(result) > 1:
        print("It wont work either!!")
    else:
        u.save()
        # gigs.gig_click_count = gigs.gig_click_count + 1
        # gigs.save()
    # if request.user:
    #     gigs.gig_click_count = gigs.gig_click_count + 1
    #     gigs.save()
    c = DummyUser.objects.all().count()
    args = {
        'gigs': gigs,
        'c': c
    }
    return render(request, 'gigview/gig_details.html', args)


def user_registration(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('user_login')
    args = {
        'form': form
    }
    return render(request, 'accountview/registration.html', args)



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('buying_view')
    return render(request, 'accountview/login.html')


def logoutview(request):
    logout(request)
    return redirect('get_landing_page')


@login_required(login_url='user_login')
def seller_profile(request):
    return render(request, 'accountview/seller.html')


