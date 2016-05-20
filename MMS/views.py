from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from MMS.models import Vinyl



from .forms import AddVinylForm


def index(request):
    return render(request, 'MMS/index.html')

def user_dashboard(request):
    return render(request, 'MMS/user_dashboard.html')

def libraries(request):
    return render(request, 'MMS/libraries.html')

def vinyls(request):
    vinyls = Vinyl.objects.order_by('artist', 'year', 'title')

    if request.method == 'POST':
        new_form = AddVinylForm()
        form = AddVinylForm(request.POST)

        if form.is_valid():
            vinyl = form.save()

            return HttpResponseRedirect(request, 'MMS/vinyls.html', {
                'vinyls': vinyls,
                'form': new_form,
            })
    else:
        form = AddVinylForm()

    return render(request, 'MMS/vinyls.html', {
        'vinyls': vinyls,
        'form': form,
    })

def vinyl_detail(request, id):
    try:
        vinyl = Vinyl.objects.get(id=id)
    except Vinyl.DoesNotExist:
        raise Http404('This vinyl does not exist')
    return render(request, 'MMS/vinyl_detail.html', {
        'vinyl': vinyl,
    })


def by_artist(request):
    vinyls = Vinyl.objects.all()
    artists = []
    temp = []

    for vinyl in vinyls:
        temp.append(vinyl)
        if vinyl.artist not in temp:
            artists.append(vinyl)

    for item in artists:
        print(item.artist)


    return render(request, 'MMS/vinyls.html')


def movies(request):
    return render(request, 'MMS/movies.html')

def video_games(request):
    return render(request, 'MMS/video_games.html')

def books(request):
    return render(request, 'MMS/books.html')