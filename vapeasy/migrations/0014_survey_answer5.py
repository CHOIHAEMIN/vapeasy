# Generated by Django 3.1.3 on 2022-05-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapeasy', '0013_auto_20220518_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='answer5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]