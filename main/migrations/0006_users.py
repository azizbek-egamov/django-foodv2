# Generated by Django 5.0.6 on 2024-08-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_adminid_cardinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='Foydalanuvchi ID')),
                ('username', models.CharField(max_length=200, verbose_name='Username')),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
