# Generated by Django 3.2.16 on 2022-11-30 10:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]