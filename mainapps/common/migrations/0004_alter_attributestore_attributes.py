# Generated by Django 5.0.4 on 2024-05-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_rename_name_value_value_attributestore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributestore',
            name='attributes',
            field=models.JSONField(default=dict),
        ),
    ]
