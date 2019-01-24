# Generated by Django 2.1.3 on 2019-01-21 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.CharField(max_length=8)),
                ('strength', models.CharField(max_length=8)),
                ('base_price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Liquid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taste', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2550)),
                ('is_nic_salt', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoldItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='inv_owner',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='item',
            name='is_nic_salt',
        ),
        migrations.RemoveField(
            model_name='item',
            name='strength',
        ),
        migrations.RemoveField(
            model_name='item',
            name='title',
        ),
        migrations.RemoveField(
            model_name='item',
            name='volume',
        ),
        migrations.AddField(
            model_name='item',
            name='owner_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='selling_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='solditems',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Item'),
        ),
        migrations.AddField(
            model_name='solditems',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bottle',
            name='liquid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Liquid'),
        ),
        migrations.AddField(
            model_name='item',
            name='bottles',
            field=models.ManyToManyField(to='employee.Bottle'),
        ),
    ]
