# Generated by Django 4.2.3 on 2023-07-25 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0015_alter_memberdata_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentdata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='memberdata',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]