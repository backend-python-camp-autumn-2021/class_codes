from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView

from .models import HandProduct, HandProductComment
from .forms import CommentForm

class HandProductListView(ListView):
    model = HandProduct
    template_name = "product_present/product_list.html"
    context_object_name = 'hand_products'
    paginate_by = 10
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
    login_url = '/profile/user/'

    def get(self, request, id):
        product = get_object_or_404(HandProduct, id = id)
        if request.user.hand_product_comments.all().filter(hand_product=product).exists():
            form = CommentForm(instance = request.user.hand_product_comments.all().get(hand_product=product))
        else:
            form = CommentForm()
        return render(request, "product_present/comment_change.html", {"form":form , "id":id})

    def post(self, request, id):
        hand_product = get_object_or_404(HandProduct, id=id)
        if request.user.hand_product_comments.all().filter(hand_product=hand_product).exists():
            form = CommentForm(request.POST or None, instance=get_object_or_404( HandProductComment , user=request.user, hand_product = hand_product))
        else:
            form = CommentForm(request.POST)
            form.instance.user = request.user
            form.instance.hand_product = hand_product
        if form.is_valid():
            try:
                form.save()
                return HttpResponse("damet garm")
            except Exception as e:
                raise IntegrityError(e)
        return render(request, "product_present/comment_change.html", {"form":form})
