from django.urls import path
from . import views

urlpatterns = [
	path("",views.Home,name='home'),
	path('detail/<int:todo_id>',views.detail,name='details'),
	path('delete/<int:todo_id>',views.delete,name='delete'),
	path("create/",views.create,name='create'),
]