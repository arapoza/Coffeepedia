from django.urls import path
from .views import signup_view, EmailLoginView
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', EmailLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
