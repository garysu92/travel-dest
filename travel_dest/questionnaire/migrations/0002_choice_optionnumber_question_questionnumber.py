# Generated by Django 4.2.4 on 2023-08-20 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='optionNumber',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='question',
            name='questionNumber',
            field=models.IntegerField(default=-1),
        ),
    ]