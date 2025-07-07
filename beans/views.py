from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic

from .models import Bean
from .forms import BeanForm
from users.forms import ReviewForm
from users.models import Review

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
        beans_form = BeanForm(request.POST, request.FILES)
        if beans_form.is_valid():
            beans_form.save()
            return render(request, "beans/partials/beans-list.html", 
                          {"bean_list": Bean.objects.all()})
        else:
            return render(request, "beans/partials/add-beans.html", 
                          {"beans_form": beans_form})
    # If the request is not a POST, render the form for adding beans
    else:
        return render(request, "beans/partials/add-beans.html", 
                      {"beans_form": BeanForm()})

def add_review(request, bean_id):
    """View to handle adding a review for a specific bean."""
    bean = get_object_or_404(Bean, pk=bean_id)
    
    if request.method == "POST":
        content = request.POST.get("content")
        rating = request.POST.get("rating")
        
        if content and rating:
            bean.reviews.create(user=request.user, content=content, rating=rating)
            return render(request, "beans/partials/reviews-list.html", 
                          {"reviews": bean.reviews.all(), "bean": bean})
        else:
            return HttpResponse("Invalid review data", status=400)
    
    return render(request, "beans/partials/add-review.html", {"bean": bean, "review_form": ReviewForm()})

def edit_review(request, review_id):
    """View to handle editing an existing review."""
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return render(request, "beans/partials/reviews-list.html", 
                          {"reviews": review.bean.reviews.all(), "bean": review.bean})
        else:
            return render(request, "beans/partials/edit-review.html", 
                          {"review_form": review_form, "review": review})
    
    review_form = ReviewForm(instance=review)
    return render(request, "beans/partials/edit-review.html", {"review_form": review_form, "review": review})

def delete_review(request, review_id):
    """View to handle deleting an existing review."""
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    
    if request.method == "POST":
        bean = review.bean
        review.delete()
        return render(request, "beans/partials/reviews-list.html", 
                      {"reviews": bean.reviews.all()})
    
    return HttpResponse("Method not allowed", status=405)