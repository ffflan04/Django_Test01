# Generated by Django 4.2.3 on 2023-08-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0028_delete_memberdata_delete_userdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Self_Introduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
        ),
    ]
