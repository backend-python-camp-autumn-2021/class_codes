from django.urls import path

from .views import HandProductListView, HandProductDetailView, CommentFormView

urlpatterns = [
    path('handproducts/', HandProductListView.as_view(), name='hand-product-list'),
    path('handproduct/<str:slug>/', HandProductDetailView.as_view(), name='hand-product-detail'),
    path('commnet/<int:id>', CommentFormView.as_view(), name='comment-change'),
]