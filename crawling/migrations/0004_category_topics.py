# Generated by Django 3.2 on 2021-06-04 14:26

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('crawling', '0003_auto_20210604_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='topics',
            field=picklefield.fields.PickledObjectField(blank=True, editable=False, null=True),
        ),
    ]
