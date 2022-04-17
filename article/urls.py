from django.urls import path, include

from rest_framework.routers import DefaultRouter

from article import views


router = DefaultRouter()


urlpatterns = [
    path('article/', views.ArticleViewSet.as_view()),
]