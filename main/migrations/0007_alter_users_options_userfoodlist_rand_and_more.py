# Generated by Django 5.0.6 on 2024-08-22 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Foydalanuvchi', 'verbose_name_plural': 'Foydalanuvchilar'},
        ),
        migrations.AddField(
            model_name='userfoodlist',
            name='rand',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Telefon'),
        ),
    ]
