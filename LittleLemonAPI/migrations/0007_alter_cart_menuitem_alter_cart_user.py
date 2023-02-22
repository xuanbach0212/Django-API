# Generated by Django 4.1.4 on 2022-12-21 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LittleLemonAPI', '0006_alter_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='menuitem',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='LittleLemonAPI.menuitem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
