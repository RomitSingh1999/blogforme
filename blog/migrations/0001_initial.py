# Generated by Django 3.0.4 on 2020-05-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('blo', models.TextField()),
                ('date', models.IntegerField()),
                
            ],
        ),
    ]
