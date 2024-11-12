from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('users/', views.profile_list),
    path('users/<int:pk>/', views.profile_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)