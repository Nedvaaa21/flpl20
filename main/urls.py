from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index_start, name= 'start'),
    # path('tab', views.index_tab, name= 'main'),
    path('tab', IndexTab.as_view(), name= 'main'),
    path('soft/<int:id>/view', views.soft_view, name='soft_view'),
    path('soft/<int:id>/edit/', views.soft_edit, name='soft_edit'),
    path('soft/<int:id>/delete/', views.soft_delete, name='soft_delete'),
    path('about-us/', views.about, name= 'about'),
    path('create/', views.create, name= 'create'),
]
