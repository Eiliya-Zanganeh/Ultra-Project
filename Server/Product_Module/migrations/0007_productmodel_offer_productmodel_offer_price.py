# Generated by Django 5.0.4 on 2024-06-24 09:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Module', '0006_productmodel_visits'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='offer',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='درصد تخفیف'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='offer_price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True, verbose_name='قیمت پس از تخفیف'),
        ),
    ]