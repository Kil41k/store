from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from product.models import Products, ProductCategories, Basket
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView



class IndexView(TemplateView):
    template_name = "products/index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Store'
        return context

class ProductsListView(ListView):
    model = Products
    template_name = "products/products.html"
    paginate_by = 3
    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context["title"] = 'Store-products'
        context['categories'] = ProductCategories.objects.all()
        return context
    

@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])