# Generated by Django 4.1.2 on 2023-01-06 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0016_alter_paper_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='organised_date',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
