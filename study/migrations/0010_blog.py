# Generated by Django 3.1.6 on 2021-05-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0009_helpful'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200, null=True)),
                ('topic', models.CharField(max_length=200, null=True)),
                ('blogc', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]