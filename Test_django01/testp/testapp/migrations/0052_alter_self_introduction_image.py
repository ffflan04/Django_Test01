# Generated by Django 4.2.3 on 2023-08-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0051_alter_image_strage_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='self_introduction',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
