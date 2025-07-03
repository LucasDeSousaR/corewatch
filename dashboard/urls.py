from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('lpar/<str:lpar_id>/', views.lpar_detail, name='lpar_detail'),
    path('grafico-lpar/<str:lpar_id>/', views.lpar_chart, name='lpar_chart'),
    path('lpars/', views.lpar_list, name='lpar_list'),
]
