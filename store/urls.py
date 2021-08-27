from django.urls import path
from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('sepet/', views.sepet, name="sepet"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/',views.processOrder, name="process_order")
	


]