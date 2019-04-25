from django.conf.urls import url, include
from .views import all_features, add_feature, feature_details


urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^new/$', add_feature, name='new_feature'),
    url(r'^(?P<pk>\d+)/$', feature_details, name='feature_details'),
    ]