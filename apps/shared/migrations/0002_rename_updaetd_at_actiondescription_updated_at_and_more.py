# Generated by Django 5.1.1 on 2024-11-06 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actiondescription',
            old_name='updaetd_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='actionmodel',
            old_name='updaetd_at',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='fieldactionmapping',
            old_name='updaetd_at',
            new_name='updated_at',
        ),
    ]
