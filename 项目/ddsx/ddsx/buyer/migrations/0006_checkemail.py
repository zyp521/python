# Generated by Django 2.2.1 on 2020-10-19 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0005_orders_ordersdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailname', models.CharField(max_length=32)),
                ('authcode', models.CharField(max_length=32)),
                ('etime', models.DateTimeField()),
            ],
        ),
    ]
