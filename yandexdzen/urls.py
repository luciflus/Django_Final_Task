"""yandexdzen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from accounts import views as acc_view
from posts import views as posts_view

acc_router = DefaultRouter()
acc_router.register('register', acc_view.AuthorViewSet)

posts_router = DefaultRouter()
posts_router.register('posts', posts_view.PostViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="final_task",
      default_version='v-0.01-beta',
      description="final_task",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="team@inbox.ru"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include(acc_router.urls)),
    path('api/account/token', obtain_auth_token),
    path('api/auth/', include('rest_framework.urls')),

    path('api/', include(posts_router.urls)),
    path('api/comments/', posts_view.CommentListCreateAPIView.as_view()),
    path('api/comments/<int:pk>/', posts_view.CommentRetrieveUpdateDestroyAPIView.as_view()),

# documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_doc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc_doc'),

]
