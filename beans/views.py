from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Bean

# Create your views here.


def index(request):
    bean_list = Bean.objects.all()
    context = {"bean_list": bean_list}
    return render(request, "beans/index.html", context)


def detail(request, bean_id):
    bean = get_object_or_404(Bean, pk=bean_id)
    return render(request, "beans/detail.html", {"bean": bean})
