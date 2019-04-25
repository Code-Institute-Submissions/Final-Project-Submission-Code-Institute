from django.conf.urls import url, include
from .views import all_bugs, add_bug, bug_details


urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^new/$', add_bug, name='new_bug'),
    url(r'^(?P<pk>\d+)/$', bug_details, name='bug_details'),
    ]