# Generated by Django 4.2.1 on 2024-01-30 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'ordering': ['-time_create']},
        ),
        migrations.AddField(
            model_name='cars',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
        migrations.AddIndex(
            model_name='cars',
            index=models.Index(fields=['-time_create'], name='cars_cars_time_cr_4cf2ef_idx'),
        ),
    ]
