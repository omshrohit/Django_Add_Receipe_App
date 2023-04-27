from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('receipes/',views.receipes,name='receipes'),
    path("delete_receipe/<id>/",views.delete_receipe,name="delete"),
    path("update_receipe/<id>/",views.update_receipe,name='update')
]


