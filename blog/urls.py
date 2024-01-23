from . import views
from django.urls import path

urlpatterns = [
    path('', views.LizardList.as_view(), name='home'),
]