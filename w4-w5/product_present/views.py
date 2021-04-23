from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import HandProduct


class HandProductListView(ListView):
    model = HandProduct
    template_name = "product_present/product_list.html"
    context_object_name = 'hand_products'
    paginate_by = 1
    # queryset = HandProduct.objects.filter(category__name="خوراکی")

    # def get_queryset(self):
    #     query_set = super().get_queryset()
    #     return query_set.filter(category__name="خوراکی")


class HandProductDetailView(DetailView):
    model = HandProduct
    template_name = "product_present/product_detail.html"
    context_object_name = 'hand_product'

