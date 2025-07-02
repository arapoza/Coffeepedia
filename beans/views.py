from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic

from .models import Bean
from .forms import BeanForm

# Create your views here.
"""
def index(request):
    bean_list = Bean.objects.all()
    context = {"bean_list": bean_list}
    return render(request, "beans/index.html", context)
"""
class IndexView(generic.ListView):
    template_name = "beans/index.html"
    context_object_name = "bean_list"

    def get_queryset(self):
        return Bean.objects.all()

class DetailView(generic.DetailView):
    model = Bean
    template_name = "beans/bean-detail.html"

def detail(request, bean_id):
    bean = get_object_or_404(Bean, pk=bean_id)
    return render(request, "beans/bean-detail.html", {"bean": bean})

def add_beans(request):
    if request.method == "POST":
        beans_form = BeanForm(request.POST)
        if beans_form.is_valid():
            beans_form.save()
            return HttpResponse("Beans added successfully!")
        else:
            return render(request, "beans/partials/add-beans.html", 
                          {"beans_form": beans_form})
    else:
        return render(request, "beans/partials/add-beans.html", 
                      {"beans_form": BeanForm()})
