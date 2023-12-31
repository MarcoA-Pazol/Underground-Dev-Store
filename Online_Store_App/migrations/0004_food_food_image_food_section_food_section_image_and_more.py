# Generated by Django 4.2.3 on 2023-07-14 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Store_App', '0003_food_section_product_section_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='food_image',
            field=models.ImageField(default='fast_food.jpg', upload_to='food_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food_section',
            name='food_section_image',
            field=models.ImageField(default='fast_food.jpg', upload_to='food_section_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='product.jpg', upload_to='product_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_section',
            name='product_section_image',
            field=models.ImageField(default='product_section.jpg', upload_to='product_section_images/'),
            preserve_default=False,
        ),
    ]
