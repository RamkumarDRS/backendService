from django.template.defaulttags import url
from django.urls import path
from setuptools.extern import names

from endpoints import views
# from endpoints.views import EndAPIView

urlpatterns = [
  # path('admin/', admin.site.urls),
  path('', views.EndpointsView ,name='EndpointsView'),
  # path('message',views.EndpointsView),
]