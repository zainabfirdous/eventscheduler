from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('create',views.create, name='form'),
    path('detail/<id>',views.detail_view,name="deatils")
]