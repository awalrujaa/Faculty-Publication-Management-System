# Generated by Django 2.2.14 on 2022-12-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0010_auto_20221224_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='organised_date',
            field=models.DateField(blank=True, default=models.CharField(blank=True, max_length=250, null=True), null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='publication_date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
