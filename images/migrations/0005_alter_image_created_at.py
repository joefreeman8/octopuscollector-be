# Generated by Django 5.0.7 on 2024-07-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_alter_image_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
