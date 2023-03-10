# Generated by Django 3.2.16 on 2023-02-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Training1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('time', models.TextField()),
                ('place', models.TextField()),
                ('training_manager', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
            ],
        ),
    ]
