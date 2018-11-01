# Generated by Django 2.1.2 on 2018-10-27 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('size', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=11)),
                ('bulk', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name_plural': 'Product',
            },
        ),
    ]