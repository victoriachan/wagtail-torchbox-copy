# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-24 08:45


from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("torchbox", "0074_servicepage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicepage",
            name="streamfield",
            field=wagtail.fields.StreamField(
                [
                    (
                        b"case_studies",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    b"title",
                                    wagtail.blocks.CharBlock(required=True),
                                ),
                                (
                                    b"intro",
                                    wagtail.blocks.TextBlock(required=True),
                                ),
                                (
                                    b"case_studies",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock(
                                            ["torchbox.WorkPage"]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        b"highlights",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    b"title",
                                    wagtail.blocks.CharBlock(required=True),
                                ),
                                (
                                    b"intro",
                                    wagtail.blocks.TextBlock(required=True),
                                ),
                                (
                                    b"highlights",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.TextBlock()
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        b"pull_quote",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    b"quote",
                                    wagtail.blocks.CharBlock(
                                        classname="quote title"
                                    ),
                                ),
                                (b"attribution", wagtail.blocks.CharBlock()),
                            ],
                            template="blocks/pull_quote_block.html",
                        ),
                    ),
                    (
                        b"process",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    b"title",
                                    wagtail.blocks.CharBlock(required=True),
                                ),
                                (
                                    b"intro",
                                    wagtail.blocks.TextBlock(required=True),
                                ),
                                (
                                    b"steps",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(
                                                        required=True
                                                    ),
                                                ),
                                                (
                                                    "icon",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Paste SVG code here",
                                                        max_length=9000,
                                                        required=True,
                                                    ),
                                                ),
                                                (
                                                    "description",
                                                    wagtail.blocks.TextBlock(
                                                        required=True
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        b"people",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    b"title",
                                    wagtail.blocks.CharBlock(required=True),
                                ),
                                (
                                    b"intro",
                                    wagtail.blocks.TextBlock(required=True),
                                ),
                                (
                                    b"people",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.PageChooserBlock()
                                    ),
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    ]
