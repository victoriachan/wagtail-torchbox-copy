# Generated by Django 2.2.17 on 2021-11-12 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0021_update_streamblock_templates"),
        ("images", "0003_alter_customimage_file_hash"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="feed_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="images.CustomImage",
            ),
        ),
    ]
