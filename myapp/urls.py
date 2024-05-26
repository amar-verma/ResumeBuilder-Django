from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login,name='login'),
    path('home/', views.home,name='home'),
    path('signup/', views.user_signup,name='user_signup'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('resume1/', views.resume1,name='resume1'),
    path('resume2/', views.resume2,name='resume2'),
    path('resume3/', views.resume3,name='resume3'),
    path('resume4/', views.resume4,name='resume4'),
    path('resume5/', views.resume5,name='resume5'),
    path('resume6/', views.resume6,name='resume6'),
    path('resume7/', views.resume7,name='resume7'),
    path('resume8/', views.resume8,name='resume8'),
    path('resume9/', views.resume9,name='resume9'),
    path('resume10/', views.resume10,name='resume10'),
    path('resume11/', views.resume11,name='resume11'),
    path('resume12/', views.resume12,name='resume12'),
    path('resume13/', views.resume13,name='resume13'),
    path('resume14/', views.resume14,name='resume14'),
    path('resume15/', views.resume15,name='resume15'),
]