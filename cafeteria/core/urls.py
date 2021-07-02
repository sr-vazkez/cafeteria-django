from django.urls import path
from . import views
urlpatterns = [
    # Paths del Core
    path('', views.home, name="home"),
    path('about/', views.home, name="about"),
    path('services/', views.home, name="services"),
    path('store/', views.home, name="store"),
    path('contact/', views.home, name="contact"),
    path('blog/', views.home, name="blog"),
    path('sample/', views.home, name="sample"),

]
