# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name='\u7269\u54c1\u7c7b\u578b')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name='\u7269\u54c1\u540d\u79f0')),
                ('price', models.IntegerField(default=0, verbose_name='\u7269\u54c1\u5355\u4ef7')),
                ('case', models.ForeignKey(to='fruit.Case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Indent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=1, verbose_name='\u7269\u54c1\u6570\u91cf')),
                ('price', models.IntegerField(default=0, verbose_name='\u7269\u54c1\u603b\u4ef7')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('goods', models.ForeignKey(to='fruit.Goods')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name='\u5e97\u5458\u59d3\u540d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='indent',
            name='person',
            field=models.ForeignKey(to='fruit.Person'),
            preserve_default=True,
        ),
    ]
