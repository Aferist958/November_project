from django.urls import path, include
from .users import urls as us_urls
# from .projects import urls as pr_urls

urlpatterns = [
    path('', include(us_urls)),
    # path('', include(pr_urls))
]
