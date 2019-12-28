from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('userChoice', views.userchoice, name='userChoice'),
    path('home/', views.home, name='home'),
    path('userChoiceDisplay', views.choicedisplay, name='userChoiceDisplay')

    # path('user_profile/<int:user_id>/', views.userprofile, name='user_profile'),
    # path('event/<int:number>/', views.eventdisplay, name='event_display'),
    # path('logout/', views.logOut, name='logOut')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
