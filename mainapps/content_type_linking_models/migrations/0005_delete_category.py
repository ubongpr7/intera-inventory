# Generated by Django 4.2.13 on 2024-05-25 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_inventorycategory_alter_inventory_category'),
        ('content_type_linking_models', '0004_remove_category_content_type_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]