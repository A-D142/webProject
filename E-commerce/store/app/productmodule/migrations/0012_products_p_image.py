# Generated by Django 5.0.2 on 2024-05-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmodule', '0011_carts_p_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='p_image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
