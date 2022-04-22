# Generated by Django 2.2.13 on 2020-11-06 10:26

from django.db import migrations
import tbx.core.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0014_contactreasonslist_is_default_not_unique"),
    ]

    operations = [
        migrations.AlterField(
            model_name="culturepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "h2",
                        wagtail.blocks.CharBlock(
                            classname="title",
                            icon="title",
                            template="patterns/molecules/streamfield/blocks/heading2_block.html",
                        ),
                    ),
                    (
                        "h3",
                        wagtail.blocks.CharBlock(classname="title", icon="title"),
                    ),
                    (
                        "h4",
                        wagtail.blocks.CharBlock(classname="title", icon="title"),
                    ),
                    (
                        "intro",
                        wagtail.blocks.RichTextBlock(
                            icon="pilcrow",
                            template="patterns/molecules/streamfield/blocks/intro_block.html",
                        ),
                    ),
                    (
                        "paragraph",
                        wagtail.blocks.RichTextBlock(
                            icon="pilcrow",
                            template="patterns/molecules/streamfield/blocks/paragraph_block.html",
                        ),
                    ),
                    (
                        "aligned_image",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("alignment", tbx.core.blocks.ImageFormatChoiceBlock()),
                                ("caption", wagtail.blocks.CharBlock()),
                                (
                                    "attribution",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                            ],
                            label="Aligned image",
                        ),
                    ),
                    (
                        "wide_image",
                        wagtail.blocks.StructBlock(
                            [("image", wagtail.images.blocks.ImageChooserBlock())],
                            label="Wide image",
                        ),
                    ),
                    (
                        "bustout",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("text", wagtail.blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                    (
                        "pullquote",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "quote",
                                    wagtail.blocks.CharBlock(
                                        classname="quote title"
                                    ),
                                ),
                                ("attribution", wagtail.blocks.CharBlock()),
                            ]
                        ),
                    ),
                    (
                        "raw_html",
                        wagtail.blocks.RawHTMLBlock(icon="code", label="Raw HTML"),
                    ),
                    ("embed", wagtail.embeds.blocks.EmbedBlock(icon="code")),
                    ("markdown", wagtailmarkdown.blocks.MarkdownBlock(icon="code")),
                ]
            ),
        ),
    ]
