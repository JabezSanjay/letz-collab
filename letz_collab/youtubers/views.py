from django.shortcuts import get_object_or_404, render
from .models import Youtuber
import urllib.parse as urlparse

# Create your views here.


def youtubers(request):
    youtubersCollection = Youtuber.objects.order_by('-created_at')
    countrySearch = Youtuber.objects.values_list(
        'country', flat=True).distinct()
    cameraModelSearch = Youtuber.objects.values_list(
        'camera_model', flat=True).distinct()
    categorySearch = Youtuber.objects.values_list(
        'category', flat=True).distinct()
    data = {
        'youtubersCollection': youtubersCollection,
        'countrySearch': countrySearch,
        'cameraModelSearch': cameraModelSearch,
        'categorySearch': categorySearch
    }
    return render(request, 'youtubers/youtubers.html', data)


def youtubers_detail(request, id):
    youtuberDetail = get_object_or_404(Youtuber, pk=id)
    videoId = video_id(youtuberDetail.videoUrl)
    youtuberDetail.videoUrl = videoId

    data = {
        'youtuberDetail': youtuberDetail,
    }
    return render(request, 'youtubers/youtubersDetail.html', data)


def youtubers_search(request):
    youtubersSearch = Youtuber.objects.order_by('-created_at')
    countrySearch = Youtuber.objects.values_list(
        'country', flat=True).distinct()
    cameraModelSearch = Youtuber.objects.values_list(
        'camera_model', flat=True).distinct()
    categorySearch = Youtuber.objects.values_list(
        'category', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            youtubersSearch = youtubersSearch.filter(name__icontains=keyword)
    if 'country' in request.GET:
        country = request.GET['country']
        if country:
            youtubersSearch = youtubersSearch.filter(country__iexact=country)
    if 'camera_model' in request.GET:
        camera_model = request.GET['camera_model']
        if camera_model:
            youtubersSearch = youtubersSearch.filter(
                camera_model__iexact=camera_model)
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            youtubersSearch = youtubersSearch.filter(category__iexact=category)

    data = {
        'youtubersSearch': youtubersSearch,
        'countrySearch': countrySearch,
        'cameraModelSearch': cameraModelSearch,
        'categorySearch': categorySearch
    }
    return render(request, 'youtubers/youtubersSearch.html', data)


def video_id(value):
    query = urlparse.urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = urlparse.parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail?
    return None
