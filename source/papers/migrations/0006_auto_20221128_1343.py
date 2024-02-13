# Generated by Django 2.2.14 on 2022-11-28 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0005_auto_20221017_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='approval_status',
            field=models.CharField(choices=[('', 'None'), ('approved', 'Approved'), ('pending', 'Pending'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]