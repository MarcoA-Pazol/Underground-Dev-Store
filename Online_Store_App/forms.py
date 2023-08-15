from django import forms

#CREATE NEW PRODUCT FORMULARY
class CreateNewProduct(forms.Form):
    product_name = forms.CharField(label="Product name: ", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    product_description = forms.CharField(label="Product description: ", max_length=600, widget=forms.Textarea(attrs={'class':'input'}))
    product_price = forms.FloatField(label="Product price:")
    product_cuantity = forms.FloatField(label="Product cuantity:")



