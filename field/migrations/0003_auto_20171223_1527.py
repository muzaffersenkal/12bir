# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-23 15:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('field', '0002_auto_20171222_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sepet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected', models.CharField(max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pay', models.IntegerField(default=0)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field', to='field.Field')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='field.Field'),
        ),
    ]