# Generated by Django 4.2.7 on 2024-01-08 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('image', models.ImageField(default='no_image.jpg', max_length=1000, upload_to='category/', verbose_name='Фотография категории')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='products.category')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Короткое описание')),
                ('popular', models.BooleanField(default=False, verbose_name='Товар популярный (трендовый)?')),
                ('product_day', models.BooleanField(default=False, verbose_name='Товар дня')),
                ('new', models.BooleanField(default=False, verbose_name='Товар новый (Новые поступления)?')),
                ('featured', models.BooleanField(default=False, verbose_name='Рекомендуемые продукты')),
                ('sale', models.BooleanField(default=False, verbose_name='Распродажа')),
                ('price', models.CharField(max_length=100, verbose_name='Цена')),
                ('old_price', models.CharField(blank=True, max_length=100, null=True, verbose_name='Старая цена')),
                ('image', models.ImageField(default='no_image.jpg', max_length=1000, upload_to='product/', verbose_name='Фотография продукта')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('title_2', models.CharField(blank=True, max_length=300, null=True, verbose_name='заголовок для описания')),
                ('description_2', models.TextField(blank=True, null=True, verbose_name='Подробное описание')),
                ('about_product_image', models.ImageField(default='no_image.jpg', max_length=1000, upload_to='product/', verbose_name='Фотография продукта для описания')),
                ('category', models.ManyToManyField(related_name='category_products', to='products.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ImagesProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_2', models.ImageField(default='no_image.jpg', max_length=1000, upload_to='product/', verbose_name='Фотография продукта')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_product', to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Фотография продукта',
                'verbose_name_plural': 'Фотографии продуктов',
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название характеристики')),
                ('value', models.CharField(max_length=300, verbose_name='Значение характеристики')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characteristics', to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
    ]