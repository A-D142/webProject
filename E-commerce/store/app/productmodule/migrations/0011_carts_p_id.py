# Generated by Django 5.0.2 on 2024-05-19 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmodule', '0010_remove_carts_p_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='p_id',
            field=models.IntegerField(default=0),
        ),
    ]