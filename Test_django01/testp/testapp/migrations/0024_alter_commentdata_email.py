# Generated by Django 4.2.3 on 2023-07-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0023_alter_commentdata_email_alter_commentdata_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentdata',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
