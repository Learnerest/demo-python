# Generated by Django 3.1.2 on 2020-12-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201216_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='context',
            field=models.TextField(default='Lorem ipsum...', max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Dummy Title', max_length=10),
        ),
    ]
