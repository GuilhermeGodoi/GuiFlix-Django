# Generated by Django 4.1.6 on 2023-04-27 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='ano',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='filme',
            name='recomendacao',
            field=models.IntegerField(),
        ),
    ]
