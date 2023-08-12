from django.db import models

# Create your models here.
#PRODUCT SECTIONS MODEL
class Product_Section(models.Model):
    product_section_name = models.CharField(max_length=200)
    product_section_description = models.TextField()
    product_section_image = models.ImageField(upload_to='product_section_images/')

    def __str__(self):
        return self.product_section_name

#PRODUCTS MODEL
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_section = models.ForeignKey(Product_Section, on_delete=models.CASCADE)
    product_price = models.FloatField()
    product_cuantity = models.FloatField()
    product_creation_date = models.DateField(auto_now_add=True)
    product_image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.product_name + ' - ' + self.product_section.product_section_name

#QUESTIONS MODEL
class Questions(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
#USERS MODEL
class Users(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=200)
    user_password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name
    
    
