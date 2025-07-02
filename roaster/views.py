from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic

from .models import Roaster
from .forms import RoasterForm

# Create your views here.
"""
def index(request):
    roaster_list = Roaster.objects.all()
    context = {"roaster_list": roaster_list}
    return render(request, "roaster/index.html", context)
"""
class IndexView(generic.ListView):
    template_name = "roaster/index.html"
    context_object_name = "roaster_list"

    def get_queryset(self):
        return Roaster.objects.all()

class DetailView(generic.DetailView):
    model = Roaster
    template_name = "roaster/roaster-detail.html"

def add_roaster(request):
    if request.method == "POST":
        country_id = request.POST.get("country")
        region_id = request.POST.get("region")
        roaster_form = RoasterForm(request.POST, country_id=country_id,
                                    region_id=region_id)
        if roaster_form.is_valid():
            roaster_form.save()
            return HttpResponse("Roaster added successfully!")
        else:
            return render(request, roaster_form.errors)
    else:
        return render(request, "roaster/partials/add-roaster.html",
                      {"roaster_form": RoasterForm()})

def region_dropdown(request):
    country_id = request.GET.get('country')
    form = RoasterForm(request.GET or None, country_id=country_id)
    return render(request, "roaster/partials/region-dropdown.html", {"form": form})

def city_dropdown(request):
    country_id = request.GET.get('country')
    region_id = request.GET.get('region')
    form = RoasterForm(request.GET or None, country_id=country_id,
                       region_id=region_id)
    return render(request, "roaster/partials/city-dropdown.html", {"form": form})