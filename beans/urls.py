from django.urls import path

from . import views

app_name = "beans"
urlpatterns = [
        path("", views.IndexView.as_view(), name="index"),
        path("<int:pk>", views.DetailView.as_view(), name="detail"),
        path("add-beans", views.add_beans, name="add_beans"),
        path("add-review/<int:bean_id>", views.add_review, name="add_review"),
]
