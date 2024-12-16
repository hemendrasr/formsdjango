from django.urls import path
from . import views





urlpatterns=[
    path('', views.user_form_view, name='user_form'),
    
    
    
    path('success/', views.success_view, name='success'),
    path('users/', views.user_list_view, name='user_list'),
    path('edit/<int:user_id>/', views.edit_user_view, name='edit_user'),
    path('delete/<int:user_id>/', views.delete_user_view, name='delete_user'),
]