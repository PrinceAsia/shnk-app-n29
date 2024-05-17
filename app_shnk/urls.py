from django.urls import path
from rest_framework import routers

from app_shnk.views import (
    SHNKSystemsViewSet,
    SHNKGroupsViewSet,
    SHNKTypesViewSet,
    SHNKDocumentsViewSet,
    SHNKDocPartViewSet,
    SHNKDocPlanViewSet,
    SHNKSubPlanViewSet,
    shnk_full_search,
    shnk_rating,
)


router = routers.DefaultRouter()
router.register(r'systems', SHNKSystemsViewSet, basename='system')
router.register(r'groups', SHNKGroupsViewSet, basename='group')
router.register(r'types', SHNKTypesViewSet, basename='type')
router.register('documents', SHNKDocumentsViewSet, basename='documents')
router.register(r'parts', SHNKDocPartViewSet, basename='parts')
router.register(r'plan', SHNKDocPlanViewSet, basename='plan')
router.register(r'sub-plan', SHNKSubPlanViewSet, basename='sub-plan')


urlpatterns = router.urls

urlpatterns += [
    path('search/', shnk_full_search, name='search'),
    path('rate/<int:shnk_id>/', shnk_rating, name='rate'),
]
