from django.contrib import admin
from django.urls import path
from . import views
from .views import api
app_name = "API"

urlpatterns = [
    path('',views.details,name='Details'),
    path('api',api.as_view()),
    path('api/put',api.as_view()),
    path('admin/', admin.site.urls),
]
