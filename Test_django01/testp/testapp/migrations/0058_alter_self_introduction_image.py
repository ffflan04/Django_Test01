# Generated by Django 4.2.3 on 2023-08-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0057_alter_ff_bool_follow_switch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='self_introduction',
            name='image',
            field=models.ImageField(default='one.png', upload_to=''),
        ),
    ]
