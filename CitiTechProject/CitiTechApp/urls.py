from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
    # path('sign_up', views.signup, name='signUp'),
    # path('home/', views.home, name='home'),
    # path('user_profile/<int:user_id>/', views.userprofile, name='user_profile'),
    # path('event/<int:number>/', views.eventdisplay, name='event_display'),
    # path('logout/', views.logOut, name='logOut')
]