# Generated by Django 3.0.7 on 2020-08-01 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0005_auto_20200730_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.ImageField(upload_to='gallary/')),
            ],
        ),
    ]
