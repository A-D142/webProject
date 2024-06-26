# Generated by Django 5.0.2 on 2024-04-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=20)),
                ('phone', models.BigIntegerField(default=0)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=20)),
                ('p_count', models.IntegerField()),
                ('img_num', models.IntegerField()),
            ],
        ),
    ]
