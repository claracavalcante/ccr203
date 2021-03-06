# Generated by Django 2.2.4 on 2021-01-17 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccr_app', '0002_auto_20210117_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='has_prizes',
            field=models.BooleanField(blank=True, db_index=True, default=False),
        ),
    ]
