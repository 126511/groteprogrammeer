# Generated by Django 3.1.5 on 2021-04-22 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='link',
            field=models.CharField(default='hoii', max_length=96),
        ),
    ]