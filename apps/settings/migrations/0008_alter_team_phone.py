# Generated by Django 4.2.7 on 2024-01-14 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0007_alter_team_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='phone',
            field=models.CharField(default=1, max_length=255, verbose_name='Номер телефона (whatsapp)'),
            preserve_default=False,
        ),
    ]
