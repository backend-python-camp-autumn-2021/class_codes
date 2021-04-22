from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import HandProduct


class HandProductListView(ListView):
    model = HandProduct
    template_name = "product_present/product_list.html"
    context_object_name = 'hand_products'
    paginate_by = 10


class HandProductDetailView(DetailView):
    model = HandProduct
    template_name = "product_present/product_detail.html"
    context_object_name = 'hand_product'

