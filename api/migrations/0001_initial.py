# Generated by Django 3.1.6 on 2021-02-05 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('desc', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('sound', models.CharField(max_length=15)),
                ('desc', models.TextField(max_length=200)),
                ('habitat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.habitat')),
            ],
        ),
    ]