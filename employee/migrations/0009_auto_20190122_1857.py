# Generated by Django 2.1.3 on 2019-01-22 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0008_auto_20190122_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='user',
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
