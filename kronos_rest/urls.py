from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('kronos_rest.urls')),
]