# Generated by Django 3.0.3 on 2020-03-16 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sspanel', '0037_auto_20200310_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='vmessnode',
            name='listen_host',
            field=models.CharField(default='0.0.0.0', max_length=64, verbose_name='本地监听地址'),
        ),
    ]