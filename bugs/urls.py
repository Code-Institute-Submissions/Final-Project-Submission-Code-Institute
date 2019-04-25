from django.conf.urls import url, include
from .views import all_bugs, add_bug


urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^new/$', add_bug, name='new_bug'),
    ]