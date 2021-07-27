# Generated by Django 3.2.5 on 2021-07-26 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gig',
            name='packages',
        ),
        migrations.AddField(
            model_name='gig',
            name='packages',
            field=models.ManyToManyField(through='mainApp.GigManager', to='mainApp.Package'),
        ),
    ]
