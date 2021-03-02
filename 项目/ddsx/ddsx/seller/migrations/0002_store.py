# Generated by Django 2.2.1 on 2020-10-13 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='湛江第一烧烤小店', max_length=32)),
                ('address', models.CharField(default='广州南沙', max_length=128)),
                ('desc', models.CharField(default='好吃', max_length=128)),
                ('logo', models.ImageField(default='1.jpg', upload_to='img')),
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller')),
            ],
        ),
    ]
