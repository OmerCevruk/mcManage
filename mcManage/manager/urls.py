from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
app_name = 'manager'

urlpatterns = [
    path('', main_page, name='main_page'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('start-server/', start_minecraft_server, name='start_server'),
    path('stop-server/', stop_minecraft_server, name='stop_server'),

]
