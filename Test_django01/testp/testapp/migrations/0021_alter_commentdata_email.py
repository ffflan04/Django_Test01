# Generated by Django 4.2.3 on 2023-07-27 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0020_remove_memberdata_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentdata',
            name='email',
            field=models.EmailField(default='midori@.com', max_length=254),
        ),
    ]
