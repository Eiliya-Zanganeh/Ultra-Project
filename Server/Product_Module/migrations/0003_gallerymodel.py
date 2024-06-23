# Generated by Django 5.0.4 on 2024-06-18 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Module', '0002_productmodel_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='galleries/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Product_Module.productmodel', verbose_name='کالا')),
            ],
            options={
                'verbose_name': 'گالری محصول',
                'verbose_name_plural': 'گالری محصولات',
                'db_table': 'gallery',
                'ordering': ['id'],
            },
        ),
    ]
