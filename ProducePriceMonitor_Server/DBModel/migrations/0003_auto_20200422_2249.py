# Generated by Django 2.2.6 on 2020-04-22 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DBModel', '0002_auto_20200422_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodspriceinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usergoodsinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usermonitororder',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usermonitororderhistory',
            name='id',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='self_session',
            field=models.CharField(default=0, max_length=40),
        ),
        migrations.AlterField(
            model_name='goodspriceinfo',
            name='goods_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usergoodsinfo',
            name='openid',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='openid',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usermonitororder',
            name='order_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usermonitororderhistory',
            name='order_id',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]