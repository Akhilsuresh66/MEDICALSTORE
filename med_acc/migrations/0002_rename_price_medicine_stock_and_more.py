# Generated by Django 5.0.2 on 2024-03-29 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('med_acc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='price',
            new_name='stock',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='description',
        ),
    ]
