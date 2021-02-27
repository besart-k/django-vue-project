from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'risk-type-definitions', views.RiskTypeDefinitionViewSet, basename='risk-type-definitions')
router.register(r'risk-type-data', views.RiskTypeDataViewSet, basename='risk-type-data')


urlpatterns = [
    path('', include(router.urls)),
]
