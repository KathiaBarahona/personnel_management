# Generated by Django 2.1.7 on 2019-03-17 22:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import personnel_management.apps.branch.AS3_storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('facade_image', models.FileField(blank=True, null=True, storage=personnel_management.apps.branch.AS3_storage.FacadeImageStorage, upload_to='')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
