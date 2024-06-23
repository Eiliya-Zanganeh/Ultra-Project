# Generated by Django 5.0.4 on 2024-06-21 13:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Module', '0004_alter_gallerymodel_product'),
        ('User_Module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1, verbose_name='تعداد')),
                ('is_finished', models.BooleanField(default=False, verbose_name='نهایی شده / نهایی نشده')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Product_Module.productmodel', verbose_name='محصول')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سبد های خرید',
            },
        ),
    ]
