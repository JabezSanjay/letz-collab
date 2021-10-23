from django.shortcuts import render
from .models import HomepageBanner
from .models import TeamMembers


# Create your views here.


def home(request):
    homepageBanner = HomepageBanner.objects.all()
    teamMembers = TeamMembers.objects.all()
    data = {
        'homepageBanner': homepageBanner,
        'teamMembers': teamMembers
    }
    return render(request, 'webpages/home.html', data)


def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')
