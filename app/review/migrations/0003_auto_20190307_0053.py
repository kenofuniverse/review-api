# Generated by Django 2.1.7 on 2019-03-07 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_review_reviewer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='company',
            new_name='company_id',
        ),
    ]