from django.urls import path, include
from rest_framework import routers

from pesca_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewset)
router.register(r'groups', views.GroupViewset)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]