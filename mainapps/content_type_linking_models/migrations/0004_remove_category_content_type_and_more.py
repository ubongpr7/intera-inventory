# Generated by Django 4.2.13 on 2024-05-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_type_linking_models', '0003_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
