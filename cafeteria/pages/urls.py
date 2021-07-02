from django.urls import path
from . import views
urlpatterns = [
    # Paths del Core
    path('<int:page_id>/', views.page, name="page"),

]
