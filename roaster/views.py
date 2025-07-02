from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic

from .models import Roaster
from .forms import RoasterForm

# Create your views here.
class IndexView(generic.ListView):
    """View to display a list of all roasters."""
    template_name = "roaster/index.html"
    context_object_name = "roaster_list"

    def get_queryset(self):
        return Roaster.objects.all()

class DetailView(generic.DetailView):
    """View to display the details of a specific roaster."""
    model = Roaster
    template_name = "roaster/roaster-detail.html"

def add_roaster(request):
    """View to handle adding new roasters via a ModelForm."""
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
    """View to handle dynamic loading of the regions dropdown 
    in the RoasterForm based on selected country."""
    country_id = request.GET.get('country')
    form = RoasterForm(request.GET or None, country_id=country_id)
    return render(request, "roaster/partials/region-dropdown.html", {"form": form})

def city_dropdown(request):
    """View to handle dynamic loading of the cities dropdown 
    in the RoasterForm based on selected region."""
    country_id = request.GET.get('country')
    region_id = request.GET.get('region')
    form = RoasterForm(request.GET or None, country_id=country_id,
                       region_id=region_id)
    return render(request, "roaster/partials/city-dropdown.html", {"form": form})