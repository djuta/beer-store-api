from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Store, Product, Inventory
from .serializers import StoreSerializer, ProductSerializer, InventorySerializer


# Store Views
@api_view(['GET'])
def stores(request, format=None):
	"""
	Returns data on all Beer Store locations
	"""
	stores = Store.objects.all()
	serializer = StoreSerializer(stores)
	return Response(serializer.data)


@api_view(['GET'])
def store_by_id(request, store_id, format=None):
	"""
	Returns data on a Beer Store location with
	a specified store id
	"""
	stores = Store.objects.get(store_id = int(store_id))
	serializer = StoreSerializer(stores)
	return Response(serializer.data)


# Product Views
@api_view(['GET'])
def products(request, format=None):
	"""
	Returns data on all Beer Store products
	"""
	products = Product.objects.all()
	serializer = ProductSerializer(products)
	return Response(serializer.data)


@api_view(['GET'])
def product_by_id(request, product_id, format=None):
	"""
	Returns data on a Beer Store product with
	a specified product id
	"""
	product = Product.objects.get(product_id = int(product_id))
	serializer = ProductSerializer(product)
	return Response(serializer.data)


# Inventory Views
@api_view(['GET'])
def inventory(request, store_id, product_id, format=None):
	"""
	Returns inventory of a specified product at specified store
	"""
	store = Store.objects.get(store_id=int(store_id))
	product = Product.objects.get(product_id=int(product_id))
	inventory = Inventory.objects.get(store_id=store, product_id=product)
	serializer = InventorySerializer(inventory)
	return Response(serializer.data)