# Generated by Django 5.1.2 on 2024-11-16 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_rename_section_label_serviceheader_label_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceCards',
            new_name='ServiceCard',
        ),
        migrations.RenameField(
            model_name='servicecard',
            old_name='service_item_description',
            new_name='service_description',
        ),
        migrations.RenameField(
            model_name='servicecard',
            old_name='service_item_icon',
            new_name='service_icon',
        ),
        migrations.RenameField(
            model_name='servicecard',
            old_name='service_item_title',
            new_name='service_title',
        ),
    ]