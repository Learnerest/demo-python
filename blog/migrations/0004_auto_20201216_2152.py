# Generated by Django 3.1.2 on 2020-12-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201216_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Dummy Title', max_length=20),
        ),
    ]
