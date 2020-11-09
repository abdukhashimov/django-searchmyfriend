from django.urls import path, include
from user.views import UserList, UserDetail
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    # path('viewset/', include(router.urls)),
    # path('viewset/<int:pk>/', include(router.urls))

]
