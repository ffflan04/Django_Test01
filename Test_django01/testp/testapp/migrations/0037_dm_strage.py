# Generated by Django 4.2.3 on 2023-08-06 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0036_remove_personmodel_is_clever_delete_resultmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DM_strage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_user', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=200)),
                ('to_user', models.CharField(max_length=200)),
                ('time_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
