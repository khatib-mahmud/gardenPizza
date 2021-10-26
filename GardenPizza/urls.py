
from django.contrib import admin
from django.urls import path
from pizza import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('order/',views.order,name="order"),
    path('order/<int:pk>',views.edit_order,name="edit_order"),
    path('pizzas/',views.pizza,name="pizza"),
    path('api_call/',views.api_call,name="api_call"),
]
