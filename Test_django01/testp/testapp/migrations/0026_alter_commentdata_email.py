# Generated by Django 4.2.3 on 2023-07-31 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0025_alter_commentdata_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentdata',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
