# Generated by Django 3.0 on 2020-05-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_auto_20200512_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]