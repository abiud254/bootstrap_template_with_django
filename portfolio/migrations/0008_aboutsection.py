# Generated by Django 5.1.2 on 2024-11-15 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_remove_featurecard_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_label', models.CharField(default='WHO WE ARE', max_length=50)),
                ('title', models.CharField(default='Unleashing Potential with Creative Strategy', max_length=200)),
                ('description', models.TextField(default='At eStartup, we believe in transforming ideas into impact. Our team of experts brings together innovation and strategic thinking to help your business thrive in a competitive landscape.')),
                ('list_item1_icon', models.CharField(default='fa-check-circle', max_length=50)),
                ('list_item1_text', models.CharField(default='Tailored solutions for every business stage.', max_length=200)),
                ('list_item2_icon', models.CharField(default='fa-check-circle', max_length=50)),
                ('list_item2_text', models.CharField(default='Proven strategies to accelerate growth.', max_length=200)),
                ('list_item3_icon', models.CharField(default='fa-check-circle', max_length=50)),
                ('list_item3_text', models.CharField(default='Dedicated support from industry professional.', max_length=200)),
                ('button_text', models.CharField(default='Read More', max_length=50)),
                ('button_url', models.CharField(blank=True, max_length=200)),
                ('main_image', models.ImageField(help_text='Main large image', upload_to='about/')),
                ('top_right_image', models.ImageField(help_text='Top right small image', upload_to='about/')),
                ('bottom_right_image', models.ImageField(help_text='Bottom right small image', upload_to='about/')),
            ],
        ),
    ]