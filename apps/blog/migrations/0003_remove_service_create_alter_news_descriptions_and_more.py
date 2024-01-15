# Generated by Django 4.2.7 on 2024-01-15 16:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_service_alter_news_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='create',
        ),
        migrations.AlterField(
            model_name='news',
            name='descriptions',
            field=ckeditor.fields.RichTextField(verbose_name='Описание новости'),
        ),
        migrations.AlterField(
            model_name='service',
            name='descriptions',
            field=ckeditor.fields.RichTextField(verbose_name='Описание услуги'),
        ),
    ]
