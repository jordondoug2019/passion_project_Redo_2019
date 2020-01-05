from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    # path('userChoice', views.userchoice, name='userChoice'),
    path('home/', views.home, name='home'),
    path('eventDisplay/<int:pk>', views.eventdisplay, name='eventDisplay'),
    path('results', views.results, name='results'),
    path('contact', views.contact, name='contact'),
    # path('user_profile/', views.user_profile, name='user_profile'),
    path('logout/', views.logOut, name='logout'),


    # path('user_profile/<int:user_id>/', views.userprofile, name='user_profile'),
    # path('event/<int:number>/', views.eventdisplay, name='event_display'),
    # path('logout/', views.logOut, name='logOut')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
