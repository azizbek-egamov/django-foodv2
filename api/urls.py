from django.urls import path, re_path, include
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API documentation",
        default_version="v1",
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@pyco.uz"),
        license=openapi.License(name="TOI"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", HomePage, name="home"),
    path("food/", FoodApiView.as_view(), name="food"),
    path("add/", FoodCreateApiView.as_view(), name="add"),
    path("delete/<int:pk>/", FoodDeleteApiView.as_view(), name="delete"),
    path("update/<int:pk>/", FoodUpdateApiView.as_view(), name="update"),
    path("user/", include("api.user_urls")),
    re_path(
        r"^docs(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="docs-json",
    ),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="docs"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
]
