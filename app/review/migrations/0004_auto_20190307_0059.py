# Generated by Django 2.1.7 on 2019-03-07 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_auto_20190307_0053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='company_id',
            new_name='company',
        ),
    ]