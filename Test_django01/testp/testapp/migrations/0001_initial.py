# Generated by Django 4.2.3 on 2023-07-17 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BulletinBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('sex', models.BooleanField()),
            ],
        ),
    ]
