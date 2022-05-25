from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.main, name='main'),
    path('contact us/', views.contactus, name='contactus'),
    path('meeting/', views.meeting, name='meeting'),
    path('commit/', views.commit, name='commit')
]
