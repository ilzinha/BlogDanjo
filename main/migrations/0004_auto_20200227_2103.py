# Generated by Django 3.0.3 on 2020-02-28 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200227_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postagem',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
