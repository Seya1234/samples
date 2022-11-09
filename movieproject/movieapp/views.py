from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    m = Movie.objects.all()
    content = {'movie_list': m}
    return render(request, 'index.html', content)


def details(request, movie_id):
    m_value = Movie.objects.get(id=movie_id)
    return render(request, "details.html", {'m_key': m_value})


def add_movie(request):
    if request.method == "POST":
        name1 = request.POST.get('name', )
        year1 = request.POST.get('year', )
        desc1 = request.POST.get('desc', )
        short_desc1 = request.POST.get('short_desc', )
        img1 = request.FILES['img']
        movie = Movie(name=name1, year=year1, desc=desc1, img=img1, short_desc=short_desc1)
        movie.save()
    return render(request, "add.html")


def update(request, id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request, id):
    if request.method =='POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
