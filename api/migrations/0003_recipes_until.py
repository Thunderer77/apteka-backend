# Generated by Django 4.2.6 on 2024-02-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_checks_sum_medicine_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='until',
            field=models.DateField(default='2023-01-01'),
            preserve_default=False,
        ),
    ]
