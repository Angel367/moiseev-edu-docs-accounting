# Generated by Django 5.0.6 on 2024-05-13 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moiseev_edu_docs_accounting_backend_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='content',
            new_name='description',
        ),
    ]
