# Generated by Django 5.0.4 on 2024-06-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Module', '0004_alter_gallerymodel_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='count',
            field=models.PositiveIntegerField(default=0, verbose_name='تعداد در انبار'),
        ),
    ]
