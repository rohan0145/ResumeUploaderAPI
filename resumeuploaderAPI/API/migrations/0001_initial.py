# Generated by Django 4.1.3 on 2023-01-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('DOB', models.DateField()),
                ('State', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=10)),
                ('pimage', models.ImageField(blank=True, upload_to='pimages')),
                ('rdoc', models.FileField(blank=True, upload_to='rdocs')),
            ],
        ),
    ]