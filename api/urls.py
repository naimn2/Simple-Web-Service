from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('habitats', views.HabitatViewSet)
router.register('animals', views.AnimalViewSet)
# router.register('animals/<filt>/', views.AnimalViewSet)

# habitat_list = views.HabitatViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# habitat_detail = views.HabitatViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# animal_list = views.AnimalViewSet.as_view({
#     'get':'list',
#     'post':'create',
# })
# animal_detail = views.AnimalViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

urlpatterns = [
    # path('habitats', habitat_list, name='habitat-list'),
    # path('habitats/<int:pk>', habitat_detail, name='habitat-detail'),
    # path('animals', animal_list, name='animal-list'),
    # path('animals/<int:pk>', animal_list, name='animal-detail'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('animals/<name>', animal_list, name='animal-list'),
    # path('animals/<name>/', animal_list, name='animal-list'),
    path('', include(router.urls)),
]