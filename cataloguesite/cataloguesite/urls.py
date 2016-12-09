from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^catalogue/', include('catalogue.urls')),
    url(r'^admin/', admin.site.urls),
]
