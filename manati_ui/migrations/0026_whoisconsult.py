# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-08 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import jsonfield.fields
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('manati_ui', '0025_whoisconsult_deleting'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoisConsult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created_at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated_at')),
                ('query_node', models.CharField(max_length=100)),
                ('query_type', models.CharField(choices=[('ip', 'IP'), ('domain', 'Domain')], max_length=20)),
                ('info_report', jsonfield.fields.JSONField(null=True)),
                ('features_info', jsonfield.fields.JSONField(null=True)),
                ('object_id', models.IntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'manati_whois_consults',
            },
        ),
    ]