from django.urls import path, include
from interests.views import InterestList, InterestDetail
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('interest/', InterestList.as_view()),
    path('interest/<int:pk>/', InterestDetail.as_view()),
    # path('viewset/', include(router.urls)),
    # path('viewset/<int:pk>/', include(router.urls))

]
