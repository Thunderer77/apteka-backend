# Generated by Django 5.0.2 on 2024-02-18 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checks',
            name='sum',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicine',
            name='price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]