# Generated by Django 3.1 on 2020-08-12 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0004_auto_20200812_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rss',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rss.user'),
        ),
    ]
