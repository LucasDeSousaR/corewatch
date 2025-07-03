from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('', views.index, name='index'),
    path('lpar/<int:lpar_id>/', views.lpar_detail, name='lpar_detail'),
]
