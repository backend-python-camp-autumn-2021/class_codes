from django import forms

from .models import HandProductComment


class CommentForm(forms.ModelForm):
    # text = forms.CharField(widget=forms.Textarea,required=False, error_messages={"required":"bayad por mikardi"})
    class Meta:
        model = HandProductComment
        exclude = ("user", "hand_product",)