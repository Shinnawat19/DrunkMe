# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=100)),
                ('rating', models.IntegerField(default=0)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('logo', models.ImageField(blank=True, upload_to='images/bar')),
                ('image1', models.ImageField(blank=True, upload_to='images/bar')),
                ('image2', models.ImageField(blank=True, upload_to='images/bar')),
                ('image3', models.ImageField(blank=True, upload_to='images/bar')),
                ('image4', models.ImageField(blank=True, upload_to='images/bar')),
                ('image5', models.ImageField(blank=True, upload_to='images/bar')),
                ('status', models.CharField(default='open', max_length=50)),
                ('promotion', models.CharField(blank=True, max_length=100)),
                ('happyhours', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/event')),
                ('name', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=100)),
                ('ticket', models.CharField(default='free', max_length=50)),
                ('date', models.DateTimeField()),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('bar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DrunkMe.Bar')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=100)),
                ('rating', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('bar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DrunkMe.Bar')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=50, null=True)),
                ('userPassword', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('point', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='images/user')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DrunkMe.User'),
        ),
    ]