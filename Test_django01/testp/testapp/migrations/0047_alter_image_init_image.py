# Generated by Django 4.2.3 on 2023-08-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0046_alter_image_init_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_init',
            name='image',
            field=models.ImageField(default='media/rubii.png', upload_to=''),
        ),
    ]
