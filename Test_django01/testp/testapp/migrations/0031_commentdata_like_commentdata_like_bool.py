# Generated by Django 4.2.3 on 2023-08-03 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0030_alter_self_introduction_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentdata',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='commentdata',
            name='like_bool',
            field=models.BooleanField(default=False),
        ),
    ]
