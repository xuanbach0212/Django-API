# Generated by Django 4.1.4 on 2022-12-21 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonAPI', '0002_cur_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
