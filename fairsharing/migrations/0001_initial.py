# Generated by Django 2.1.5 on 2019-02-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FairsharingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('abbreviation', models.CharField(max_length=128)),
                ('doi', models.TextField(blank=True, max_length=27, null=True)),
                ('homepage', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
    ]