# Generated by Django 3.1.3 on 2022-05-18 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vapeasy', '0012_auto_20220512_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='category',
            new_name='choice',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='menthol',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='sweet',
        ),
    ]
