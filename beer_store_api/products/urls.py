from django.conf.urls import patterns, url

from products import views

urlpatterns = patterns("",
	# /stores
	url(
		regex=r"^stores/$",
		view=views.stores,
		name="beer_store_api"
	),

	# /stores/:store_id
	url(
		regex=r"^stores/(?P<store_id>[0-9]+)/$",
		view=views.store_by_id,
		name="beer_store_api"
	),

	# /inventory/:store_id/:product_id
	url(
		regex=r"^stores/(?P<store_id>[0-9]+)/products/(?P<product_id>[0-9]+)/inventory/$",
		view=views.inventory,
		name="beer_store_api"
	),
)
