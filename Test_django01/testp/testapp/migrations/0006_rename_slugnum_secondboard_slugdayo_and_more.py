# Generated by Django 4.2.3 on 2023-07-21 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_secondboard_likefood_secondboard_myhoby'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secondboard',
            old_name='slugnum',
            new_name='slugdayo',
        ),
        migrations.AddField(
            model_name='bulletinboard',
            name='slugnum',
            field=models.SlugField(null=True),
        ),
    ]