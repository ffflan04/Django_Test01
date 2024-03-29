# Generated by Django 4.2.3 on 2023-08-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0031_commentdata_like_commentdata_like_bool'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedBool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('byuser', models.CharField(max_length=200)),
                ('tweet', models.CharField(max_length=200)),
                ('like_bool', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='commentdata',
            name='like_bool',
        ),
    ]
