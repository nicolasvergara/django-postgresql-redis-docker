from django.urls import path, include

from rest_framework.routers import DefaultRouter

from account import views


router = DefaultRouter()
router.register('account', views.UserAccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]