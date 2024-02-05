from . import views
from django.urls import path

urlpatterns = [
    path('', views.LizardList.as_view(), name='home'),
    path('<slug:slug>/', views.LizardDetail.as_view(), name='lizard_detail'),
    path('like/<slug:slug>', views.LizardLike.as_view(), name='lizard_like'),
    path('<slug:slug>/<int:pk>/delete_experience/',
         views.ExperienceDelete.as_view(), name="delete_experience"),
    path('<slug:slug>/<int:pk>/edit_experience/',
         views.ExperienceEdit.as_view(), name="edit_experience"),
    path('403', views.Page403.as_view(), name='403'),
    path('404', views.Page404.as_view(), name='404'),
]

