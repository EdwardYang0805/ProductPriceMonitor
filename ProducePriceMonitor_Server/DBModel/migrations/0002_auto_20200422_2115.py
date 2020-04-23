# Generated by Django 2.2.6 on 2020-04-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsPriceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.CharField(max_length=30)),
                ('platform', models.CharField(max_length=10)),
                ('time', models.DateTimeField(auto_now=True)),
                ('price', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserGoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=30)),
                ('begin_time', models.DateTimeField(auto_now=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('platform', models.CharField(max_length=10)),
                ('goods_id', models.CharField(max_length=30)),
                ('monitor_user', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=30)),
                ('session_key', models.CharField(max_length=30)),
                ('unionid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserMonitorOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=30)),
                ('begin_time', models.DateTimeField(auto_now=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('goods_list', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='UserMonitorOrderHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=30)),
                ('begin_time', models.DateTimeField(auto_now=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('goods_list', models.CharField(max_length=2048)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
