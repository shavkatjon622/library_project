from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view   # swagger qoshimcha tools API larni frontend yoki mobile dasturchilar qiynalmasdan tushunishi va ishlatishi uchun
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Book list API",
        default_version='v1',
        description="Library demo project",
        terms_of_service='demo.com',
        contact=openapi.Contact(email='shavkatjonvahhobov@gmail.com'),
        license=openapi.License(name="demo license"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('api-auth/', include('rest_framework.urls')), # bu ikki endpoint orqali login va logout qismlarni loyihamizga qoshdik
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), # bu qism registratsiya uchun restni ozidan olindi

    # swagger
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0,)),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0,)),
]
