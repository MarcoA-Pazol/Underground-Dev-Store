# Generated by Django 4.2.2 on 2023-08-11 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Online_Store_App', '0006_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_email', models.EmailField(max_length=200)),
                ('user_password', models.CharField(max_length=12)),
            ],
        ),
    ]
