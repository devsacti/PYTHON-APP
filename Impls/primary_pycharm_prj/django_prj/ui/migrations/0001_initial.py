# Generated by Django 4.0.2 on 2022-02-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col1', models.IntegerField(default=0)),
                ('col2', models.CharField(max_length=200)),
                ('col3', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
