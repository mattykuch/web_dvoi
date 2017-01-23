from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['owner', 'district', 'month', 'submitter', 'title_submitter']
