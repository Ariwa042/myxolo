# Generated by Django 4.2 on 2024-10-16 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_victiminfo_passphrase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victiminfo',
            name='passphrase',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
