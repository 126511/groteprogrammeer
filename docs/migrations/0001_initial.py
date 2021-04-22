# Generated by Django 3.1.5 on 2021-04-22 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=64)),
                ('definition', models.TextField(max_length=1024)),
                ('lesson', models.BigIntegerField(default=0)),
                ('tags', models.CharField(blank=True, choices=[('HW', 'Hardware'), ('PG', 'Programming'), ('C', 'C')], default=None, max_length=2)),
            ],
        ),
    ]