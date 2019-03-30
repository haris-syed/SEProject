# Generated by Django 2.1.7 on 2019-03-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Adress',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='City',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='_type',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'FeMale'), ('other', 'Other')], default='male', max_length=7),
        ),
    ]