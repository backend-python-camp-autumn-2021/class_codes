from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView

from .models import HandProduct
from .forms import CommentForm

class HandProductListView(ListView):
    model = HandProduct
    template_name = "product_present/product_list.html"
    context_object_name = 'hand_products'
    paginate_by = 1
    # queryset = HandProduct.objects.filter(category__name="خوراکی")

    # def get_queryset(self):
    #     query_set = super().get_queryset()
    #     return query_set.filter(category__name="خوراکی")
    def get_paginate_by(self, queryset):
        """
        Get the number of items to paginate by, or ``None`` for no pagination.
        """
        return int(self.request.GET.get('paginate_by', self.paginate_by))


class HandProductDetailView(DetailView):
    model = HandProduct
    template_name = "product_present/product_detail.html"
    context_object_name = 'hand_product'


class CommentFormView(LoginRequiredMixin, View):
    def get(self, request, id):
        product = get_object_or_404(HandProduct, id = id)
        if request.user.hand_product_comments.all().filter(hand_product=product).exists():
            form = CommentForm(instance = request.user.hand_product_comments.all().get(hand_product=product))
        else:
            form = CommentForm()
        return render(request, "product_present/comment_change.html", {"form":form , "id":id})

    def post(self, request, id):
        form = CommentForm(request.POST)
        if form.is_valid():
            try:
                form.instance.user = request.user
                product = get_object_or_404(HandProduct, id=id)
                form.instance.hand_product = product
                form.save()
                return HttpResponse("damet garm")
            except Exception as e:
                raise IntegrityError(e)

        return render(request, "product_present/comment_change.html", {"form":form})
