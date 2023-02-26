# Generated by Django 3.2.16 on 2023-02-11 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_training_manager1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training_manager2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('speciality', models.TextField()),
                ('number', models.IntegerField()),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
            ],
        ),
    ]