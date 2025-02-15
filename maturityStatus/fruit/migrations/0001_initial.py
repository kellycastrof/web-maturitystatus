# Generated by Django 3.1.6 on 2021-02-18 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit_type', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('path', models.CharField(max_length=250)),
                ('fruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fruit.fruit')),
            ],
        ),
    ]
