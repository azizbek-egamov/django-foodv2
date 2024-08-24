from django.urls import path
from .views import *


urlpatterns = [
    path("food/", UserFoodApiView.as_view(), name="user-food"),
    path("add/", UserFoodCreateApiView.as_view(), name="user-add"),
    path("delete/<int:pk>/", UserFoodDeleteApiView.as_view(), name="user-delete"),
    path("update/<int:pk>/", UserFoodUpdateApiView.as_view(), name="update"),
]
