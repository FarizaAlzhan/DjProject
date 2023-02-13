# Generated by Django 3.2.16 on 2023-02-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_training2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books_self_development',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.TextField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
            ],
        ),
    ]
