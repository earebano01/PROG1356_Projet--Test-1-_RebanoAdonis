# Generated by Django 4.2.6 on 2023-10-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_rename_products_product_order_customer_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Electronic', 'Electronic'), ('Fashion', 'Fashion'), ('Food', 'Food')], max_length=10, null=True),
        ),
    ]
