# Generated by Django 3.0.7 on 2020-07-08 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200705_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='p_featured',
            field=models.ImageField(default='default.jpg', upload_to='product_pics'),
        ),
    ]
