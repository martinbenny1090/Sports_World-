# Generated by Django 3.0.4 on 2020-04-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_auto_20200414_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
