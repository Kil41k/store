from django.urls import path, include
from product.views import ProductsListView, basket_add, basket_remove

app_name = 'product'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('baskets/remove/<int:id>/', basket_remove, name='basket_remove'),
]