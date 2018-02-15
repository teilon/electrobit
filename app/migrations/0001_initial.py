# Generated by Django 2.0.2 on 2018-02-13 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='category name', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='company name', max_length=20)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default='')),
                ('description_short', models.TextField(default='')),
                ('price', models.CharField(default=0, max_length=20)),
                ('price_opt', models.CharField(default=0, max_length=20)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Company')),
            ],
        ),
    ]