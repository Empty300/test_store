# Generated by Django 4.1.4 on 2022-12-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image1_alter_product_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Скидка'),
        ),
    ]
