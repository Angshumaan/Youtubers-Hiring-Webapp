from django.shortcuts import render
from .models import Youtuber
from django.shortcuts import get_object_or_404
# Create your views here.


def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')

    # for youtuber ..This is array(list) coz we have specified values_list
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list(
        'camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list(
        'category', flat=True).distinct()

    '''TuBERS HTML CODE START'''
    # pass 'city' as name ="city" in search.html
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)

    # pass 'camera_type' as name ="camera_type" in search.html
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)

    # pass 'category' as name ="category" in search.html
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(city__iexact=category)
    '''TuBERS HTML CODE End'''

    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'category_search': category_search,

    }
    # First parameter is request and second is the template ,fourth is data ..So we will create a new folder for youtuber and inside it we will have the html files . We don't have to specify templates/youtuber/h.html beacuse template is already a base directory in settings
    return render(request, 'youtubers/youtubers.html', data)


def youtubers_details(request, id):
    # model inside the brackets ...We need primary key to get the exact specifc youtuber so we are passing youtuber as model in get_object_orz-404 in youtubers_detail function
    # Note :-Firstly import get_object_or_404
    tuber = get_object_or_404(Youtuber, pk=id)

    data = {
        'tuber': tuber
    }

    return render(request, 'youtubers/youtuber_detail.html', data)


def search(request):
    # for home ... THis is all objects like key value pair in order-by
    tubers = Youtuber.objects.order_by('-created_date')

    # for youtuber ..This is array(list) coz we have specified values_list
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list(
        'camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list(
        'category', flat=True).distinct()

    '''HOME HTML CODE START'''
    # pass 'keyword' as name ="keyword" in home.hyml
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']  # grabbing the keyword
        if keyword:  # if keyword is presenet
            # Then we will update tubers globalmvaribale based on description ..Refer to queryset api to know more
            tubers = tubers.filter(description__icontains=keyword)
    '''HOME HTML CODE End'''

    '''TuBERS HTML CODE START'''
    # pass 'city' as name ="city" in search.html
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)

    # pass 'camera_type' as name ="camera_type" in search.html
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type)

    # pass 'category' as name ="category" in search.html
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(city__iexact=category)
    '''TuBERS HTML CODE End'''

    data = {
        'tubers': tubers,
        'city_search': city_search,
        'camera_type_search': camera_type_search,
        'category_search': category_search,

    }

    return render(request, 'youtubers/search.html', data)
