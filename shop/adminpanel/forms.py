from django import forms
from adminpanel.models import *


class ProductForm(forms.Form):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop')
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea())
    amount = forms.IntegerField()
    price = forms.FloatField()
    active = forms.BooleanField()
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    def __init__(self, instance, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        if instance:
            self.fields['title'].initial = instance['product'].title
            self.fields['description'].initial = instance['product'].description
            self.fields['amount'].initial = instance['product'].amount
            self.fields['price'].initial = instance['product'].price
            self.fields['active'].initial = instance['product'].active
            self.fields['categories'].initial = instance['product'].categories.all()
            for index, product_image in enumerate(instance['images'].all()):
                self.fields[f'image_{index}'] = forms.ImageField()
                self.fields[f'image_{index}'].initial = product_image.images
        else:
            self.fields['image_0'] = forms.ImageField()

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'description', 'imageUrl']
