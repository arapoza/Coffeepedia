from django.urls import path

from . import views

app_name = "beans"
urlpatterns = [
        path("", views.index, name="index"),
        path("<int:bean_id>", views.detail, name="detail"),
        path("add-beans", views.add_beans, name="add_beans"),
        path("add-roaster", views.add_roaster, name="add_roaster"),
]
