from django.conf.urls import url
from django.contrib import admin
from djangoProject import view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', view.about, name='about'),
    url(r'^$', view.home,name='home'),
]
