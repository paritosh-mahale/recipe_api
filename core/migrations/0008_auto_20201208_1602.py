# Generated by Django 3.1.4 on 2020-12-08 16:02

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201208_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to=core.models.recipe_upload_file_path),
        ),
    ]
