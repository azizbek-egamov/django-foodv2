"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name='home'),
    path("products/", ProdoctsPage, name="products"),
    path("delete/<int:user>/<int:id>", ProductDeletePage, name="delete"),
    path("edit/", UpdatePage, name="update"),
    
    path('ru/', RuHomePage, name='ruhome'),
    path("ru/products/", RuProdoctsPage, name="ruproducts"),
    path("ru/delete/<int:user>/<int:id>", RuProductDeletePage, name="rudelete"),
    path("ru/edit/", RuUpdatePage, name="ruupdate"),
    
    # path('api/v1/', include('api.urls')),
    path('api/user/addfoods/', FoodAddApi, name='food-add-api'),
    path('api/user/updatefoods/', FoodUpdateApi, name='food-update-api'),
    path('api/food/', FoodInfo, name='food-info-api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)