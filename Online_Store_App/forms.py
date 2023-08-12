from django import forms

#CREATE NEW PRODUCT FORMULARY
class CreateNewProduct(forms.Form):
    product_name = forms.CharField(label="Product name: ", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    product_description = forms.CharField(label="Product description: ", max_length=600, widget=forms.Textarea(attrs={'class':'input'}))
    product_price = forms.FloatField(label="Product price:")
    product_cuantity = forms.FloatField(label="Product cuantity:")


#CREATE NEW USER FORMULARY
class CreateNewUser(forms.Form):
    user_name = forms.CharField(label="Username: ", max_length=200)
    user_email = forms.EmailField(label="E-mail: ", max_length=200)
    user_password = forms.CharField(label="Password: ", max_length=20)

class LoginUser(forms.Form):
    user_name = forms.CharField(label="Username: ", max_length=200)
    user_password = forms.CharField(label="Password: ", max_length=20)


