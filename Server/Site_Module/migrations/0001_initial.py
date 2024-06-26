# Generated by Django 5.0.4 on 2024-05-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product_Module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=300, verbose_name='نام سایت')),
                ('site_description', models.CharField(max_length=300, verbose_name='توضیحات سایت')),
                ('description_img', models.ImageField(upload_to='description_img/', verbose_name='عکس توضیحات سایت')),
                ('how_active_user_account', models.CharField(choices=[('email', 'ایمیل'), ('phone', 'شماره تلفن')], default='email', max_length=10, verbose_name='شیوه فعال سازی حساب کاربری')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیر فعال')),
                ('popular_products', models.ManyToManyField(related_name='popular_products', to='Product_Module.productmodel', verbose_name='محصولات ویژه')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات های سایت',
                'db_table': 'site_setting',
                'ordering': ['is_active'],
            },
        ),
    ]
