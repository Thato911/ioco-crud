from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url, include
from rest_framework import routers
from backend.api import views

router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'position', views.PositionViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]