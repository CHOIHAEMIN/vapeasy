# Generated by Django 3.1.3 on 2022-07-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapeasy', '0014_survey_answer5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
