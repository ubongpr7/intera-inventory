# Generated by Django 5.0.4 on 2024-05-13 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_verificationcode_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlacklistedToken',
        ),
    ]
