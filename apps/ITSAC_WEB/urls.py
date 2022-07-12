from django.urls import path
from apps.ITSAC_WEB.views import views

urlpatterns = [
    path('', views.index, name='index'),
]