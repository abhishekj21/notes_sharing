# Generated by Django 3.1.6 on 2021-05-01 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que', models.CharField(max_length=200, null=True)),
                ('ans1', models.CharField(max_length=300, null=True)),
                ('ans2', models.CharField(max_length=300, null=True)),
                ('ans3', models.CharField(max_length=300, null=True)),
                ('ans4', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
