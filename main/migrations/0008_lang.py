# Generated by Django 5.0.6 on 2024-08-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_users_options_userfoodlist_rand_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='ID raqami')),
                ('lang', models.CharField(max_length=2)),
            ],
        ),
    ]
