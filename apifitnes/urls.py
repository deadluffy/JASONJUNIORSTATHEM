from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClubsViewSet, TarifsViewSet, GetClubsView, PersonalViewSet, TrainingViewSet, GetPersonalView
router = DefaultRouter()
router.register('clubs', ClubsViewSet, )
router.register('tarifs', TarifsViewSet )
router.register('personal', PersonalViewSet )
router.register('training', TrainingViewSet )




urlpatterns = [
    path('api/', include(router.urls)),
    path('api/clubs/filter', GetClubsView.as_view()),
    path('api/personal/filter', GetPersonalView.as_view()),
]
