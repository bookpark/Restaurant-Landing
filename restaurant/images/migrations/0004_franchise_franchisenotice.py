# Generated by Django 2.2.2 on 2019-06-27 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20190627_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_1', models.ImageField(upload_to='franchise_1')),
                ('franchise_2', models.ImageField(upload_to='franchise_2')),
                ('franchise_3', models.ImageField(upload_to='franchise_3')),
                ('franchise_4', models.ImageField(upload_to='franchise_4')),
            ],
        ),
        migrations.CreateModel(
            name='FranchiseNotice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_notice', models.ImageField(upload_to='franchise_notice')),
            ],
        ),
    ]
