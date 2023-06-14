from django.urls import path
from hhapp import views


app_name = 'hhapp'

urlpatterns = [
    path('', views.start, name='index'),
    path('form/', views.form, name='form'),
    path('result/', views.result, name='result'),
    path('area-list/', views.AreaList.as_view(),name='area_list'),
    path('area-detail/<int:pk>', views.AreaDetail.as_view(),name='area_detail'),
    path('area-create/', views.AreaCreate.as_view(),name='area_create'),
    path('area-update/', views.AreaUpdate.as_view(),name='area_update'),
    path('area-delete/', views.AreaList.as_view(),name='area_delete')
]
