from django.urls import path

from . import views

app_name = "roaster"
urlpatterns = [
        path("", views.IndexView.as_view(), name="index"),
        path("<int:pk>", views.DetailView.as_view(), name="detail"),
        path("add-roaster", views.add_roaster, name="add_roaster"),
        path('region-dropdown/', views.region_dropdown, name='region_dropdown'),
        path('city-dropdown/', views.city_dropdown, name='city_dropdown'),
]