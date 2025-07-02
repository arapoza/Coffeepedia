from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic

from .models import Bean
from .forms import BeanForm

# Create your views here.
class IndexView(generic.ListView):
    """View to display a list of all beans."""
    template_name = "beans/index.html"
    context_object_name = "bean_list"

    def get_queryset(self):
        return Bean.objects.all()

class DetailView(generic.DetailView):
    """View to display the details of a specific bean."""
    model = Bean
    template_name = "beans/bean-detail.html"

def add_beans(request):
    """View to handle adding new beans via a ModelForm."""
    # If the request is a POST, process the form data
    if request.method == "POST":
        beans_form = BeanForm(request.POST)
        if beans_form.is_valid():
            beans_form.save()
            return HttpResponse("Beans added successfully!")
        else:
            return render(request, "beans/partials/add-beans.html", 
                          {"beans_form": beans_form})
    # If the request is not a POST, render the form for adding beans
    else:
        return render(request, "beans/partials/add-beans.html", 
                      {"beans_form": BeanForm()})
