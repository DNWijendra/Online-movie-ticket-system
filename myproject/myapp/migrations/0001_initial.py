# Generated by Django 5.0.6 on 2024-06-10 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=30, null=True)),
                ('ticket_price', models.CharField(max_length=8, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='profile')),
                ('show_time', models.CharField(max_length=15, null=True)),
                ('type', models.CharField(max_length=10, null=True)),
                ('language', models.CharField(max_length=10, null=True)),
                ('release_date', models.CharField(max_length=10, null=True)),
                ('screening_type', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
