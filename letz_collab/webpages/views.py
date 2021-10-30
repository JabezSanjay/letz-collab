from django.shortcuts import render
from .models import HomepageBanner, TeamMembers
from youtubers.models import Youtuber


# Create your views here.


def home(request):
    homepageBanner = HomepageBanner.objects.all()
    teamMembers = TeamMembers.objects.all()
    featuredYoutubers = Youtuber.objects.order_by(
        '-created_at').filter(is_featured=True)
    latestYoutubers = Youtuber.objects.order_by(
        '-created_at').filter(is_featured=False)
    usersSearch = Youtuber.objects.values_list(
        'name', flat=True).distinct()
    data = {
        'homepageBanner': homepageBanner,
        'teamMembers': teamMembers,
        'featuredYoutubers': featuredYoutubers,
        'latestYoutubers': latestYoutubers,
        'usersSearch': usersSearch,
    }
    return render(request, 'webpages/home.html', data)


def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')
