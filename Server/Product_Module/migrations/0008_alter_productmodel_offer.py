# Generated by Django 5.0.4 on 2024-06-24 09:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Module', '0007_productmodel_offer_productmodel_offer_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='offer',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='درصد تخفیف'),
        ),
    ]
