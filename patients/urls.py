from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [

    #path to access the admin page
    path('admin/', admin.site.urls),

    #path to render the Home page
    path('', views.frontend, name='frontend'),
]
