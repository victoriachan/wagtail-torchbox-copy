# Generated by Django 3.2.18 on 2023-05-02 11:22

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0006_auto_20220422_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationsettings',
            name='footer_logos',
            field=wagtail.fields.StreamField([('logos', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.StreamBlock([('internal_link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(required=False))])), ('external_link', wagtail.blocks.StructBlock([('link_url', wagtail.blocks.URLBlock(label='URL')), ('link_text', wagtail.blocks.CharBlock())]))]))]))], blank=True, help_text='Single list of logos that appear before the footer box', use_json_field=True),
        ),
    ]