# Generated by Django 5.0.7 on 2024-08-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
