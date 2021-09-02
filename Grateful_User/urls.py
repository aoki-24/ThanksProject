from django.urls import path
from . import views

app_name = 'Grateful_User'
urlpatterns = [
    path('mypage/',views.mypage.as_view(),name='mypage'),
]
