from django import forms

from .models import HandProductComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = HandProductComment
        exclude = ("user", "hand_product",)