#
# Copyright (c) 2017 Stratosphere Lab.
# 
# This file is part of ManaTI Project 
# (see <https://stratosphereips.org>). It was created by 'Raul B. Netto <raulbeni@gmail.com>'
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program. See the file 'docs/LICENSE' or see <http://www.gnu.org/licenses/> 
# for copying permission.
#
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-17 11:07
from __future__ import unicode_literals

from django.db import migrations, models
import django_enumfield.db.fields
import manati_ui.models


class Migration(migrations.Migration):

    dependencies = [
        ('manati_ui', '0002_auto_20160817_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='weblog',
            name='register_status',
            field=django_enumfield.db.fields.EnumField(default=0, enum=manati_ui.models.RegisterStatus),
        ),
        migrations.AlterField(
            model_name='weblog',
            name='verdict',
            field=models.CharField(choices=[('malicious', 'Malicious'), ('legitimate', 'Legitimate'), ('suspicious', 'Suspicious'), ('undefined', 'Undefined'), ('false_positive', 'False Positive'), ('malicious_legitimate', 'Malicious/Legitimate'), ('suspicious_legitimate', 'Suspicious/Legitimate'), ('undefined_legitimate', 'Undefined/Legitimate'), ('false_positive_legitimate', 'False Positive/Legitimate'), ('undefined_malicious', 'Undefined/Malicious'), ('suspicious_malicious', 'Suspicious/Malicious'), ('false_positive_malicious', 'False Positive/Malicious'), ('false_positive_suspicious', 'False Positive/Suspicious'), ('undefined_suspicious', 'Undefined/Suspicious'), ('undefined_false_positive', 'Undefined/False Positive')], default='legitimate', max_length=20),
        ),
    ]
