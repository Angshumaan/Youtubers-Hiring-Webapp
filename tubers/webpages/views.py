from django.shortcuts import render
from .models import Slider, Team, About
# imorting from youtbers app to get data in webpages
from youtubers.models import Youtuber

# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    fetaured_youtubers = Youtuber.objects.order_by(
        '-created_date').filter(is_featured=True)  # ONly the faetured youtubers
    all_tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'sliders': sliders,
        'teams': teams,
        'featured_youtubers': fetaured_youtubers,
        'all_tubers': all_tubers,
    }
    return render(request, 'webpages/home.html', data)


def about(request):
    about = About.objects.all()
    teams = Team.objects.all()
    data = {
        "teams": teams,
        "about": about
    }
    return render(request, 'webpages/about.html', data)


def services(request):
    return render(request, 'webpages/services.html')


def contact(request):
    return render(request, 'webpages/contact.html')
