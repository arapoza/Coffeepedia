from django.urls import path

from . import views

app_name = "beans"
urlpatterns = [
        path("", views.index, name="index"),
        path("<int:bean_id>", views.detail, name="detail"),
]
