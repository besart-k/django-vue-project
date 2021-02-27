from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'risk-type-definitions', views.RiskTypeDefinitionViewSet)
router.register(r'risk-type-data', views.RiskTypeDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
