from django.urls import path
from . import views
import django.contrib.auth.views as auth


app_name = 'Grateful_Episode'
urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('logout/', auth.LogoutView.as_view(next_page='/'), name='logout'),
] 
