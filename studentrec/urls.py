from django.urls import path
from .views import (ListView, CreateView,
		DetailView, UpdateView, DeleteView
	)


urlpatterns = [
	path('', ListView, name = "home"),
	path('new/', CreateView, name = 'create'),
	path('detail/<slug:reg_no>/', DetailView, name = 'detail' ),
	path('update/<slug:reg_no>/', UpdateView, name = 'update' ),
	path('delete/<slug:reg_no>/', DeleteView, name = 'delete' ),
]