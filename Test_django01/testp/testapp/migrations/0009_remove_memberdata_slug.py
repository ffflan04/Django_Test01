# Generated by Django 4.2.3 on 2023-07-23 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_commentdata_memberdata_delete_bulletinboard_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberdata',
            name='slug',
        ),
    ]