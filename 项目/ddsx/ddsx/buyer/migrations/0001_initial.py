# Generated by Django 2.2.1 on 2020-10-15 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='zs', max_length=32)),
                ('password', models.CharField(default='111', max_length=128)),
                ('email', models.CharField(default='110@qq.com', max_length=128)),
                ('phone', models.CharField(default='110', max_length=128)),
                ('address', models.CharField(default='beijing', max_length=128)),
            ],
        ),
    ]
