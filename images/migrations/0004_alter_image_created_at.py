# Generated by Django 5.0.7 on 2024-07-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_image_options_remove_image_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
