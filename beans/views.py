from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Bean
from .forms import BeanForm, RoasterForm

# Create your views here.


def index(request):
    bean_list = Bean.objects.all()
    context = {"bean_list": bean_list}
    return render(request, "beans/index.html", context)


def detail(request, bean_id):
    bean = get_object_or_404(Bean, pk=bean_id)
    return render(request, "beans/detail.html", {"bean": bean})

def add_beans(request):
    if request.method == "POST":
        beans_form = BeanForm(request.POST)
        if beans_form.is_valid():
            beans_form.save()
            return HttpResponse("Bean added successfully!")
        else:
            return render(request, "beans/partials/add-beans.html", 
                          {"beans_form": beans_form})
    else:
        return render(request, "beans/partials/add-beans.html", 
                      {"beans_form": BeanForm()})

def add_roaster(request):
    if request.method == "POST":
        roaster_form = RoasterForm(request.POST)
        if roaster_form.is_valid():
            roaster_form.save()
            return HttpResponse("Roaster added successfully!")
        else:
            return render(request, "beans/partials/add-beans.html", 
                          {"roaster_form": roaster_form})
    else:
        return render(request, "beans/partials/add-roaster.html", {"roaster_form": RoasterForm()})