from django.urls import path

from .views import *

urlpatterns = [
    path('', NewsListAPIView.as_view(),name="api_news_list"),
    path('create/', NewsCreatedAPIView.as_view(),name="api_news_create"),
    path('update/<int:pk>/', NewsUpdateAPIView.as_view(),name="api_news_update"),
    path('destroy/<int:pk>/', NewsDestroyAPIView.as_view(),name="api_news_delete")
]