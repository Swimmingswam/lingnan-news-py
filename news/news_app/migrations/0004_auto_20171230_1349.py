# Generated by Django 2.0 on 2017-12-30 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0003_auto_20171230_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsimage',
            name='news',
        ),
        migrations.AddField(
            model_name='news',
            name='isrc',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='NewsImage',
        ),
    ]
