from django.urls import path, include
from personality.views import QuestionList, QuestionDetail, AnswerList, AnswerDetail
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('question/', QuestionList.as_view()),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    path('answer/', AnswerList.as_view()),
    path('answer/<int:pk>/', AnswerDetail.as_view()),
    # path('viewset/', include(router.urls)),
    # path('viewset/<int:pk>/', include(router.urls))

]
