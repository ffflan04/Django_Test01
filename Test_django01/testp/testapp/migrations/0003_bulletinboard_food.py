# Generated by Django 4.2.3 on 2023-07-17 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_bulletinboard_hoby'),
    ]

    operations = [
        migrations.AddField(
            model_name='bulletinboard',
            name='food',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
