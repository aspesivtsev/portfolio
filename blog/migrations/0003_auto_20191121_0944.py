# Generated by Django 2.2.7 on 2019-11-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191110_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='mod_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/blog/'),
        ),
    ]
