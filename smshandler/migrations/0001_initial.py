# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HandlerLog',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('status', models.BooleanField(verbose_name='Status', help_text='Did message sent with success?', default=True)),
                ('phone', models.CharField(verbose_name='Phone', max_length=13)),
                ('error_code', models.IntegerField(verbose_name='Error code', null=True)),
                ('error_msg', models.CharField(max_length=150, verbose_name='Error message', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Handler log',
                'verbose_name_plural': 'Handler logs',
            },
            bases=(models.Model,),
        ),
    ]
