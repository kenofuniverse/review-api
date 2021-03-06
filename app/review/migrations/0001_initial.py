# Generated by Django 2.1.7 on 2019-03-06 10:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('title', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=10000)),
                ('ip_address', models.GenericIPAddressField()),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.Company')),
            ],
            options={
                'ordering': ('-submission_date',),
            },
        ),
    ]
