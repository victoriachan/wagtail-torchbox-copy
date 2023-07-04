# Generated by Django 3.2.18 on 2023-06-26 11:26

from django.db import migrations
import tbx.core.blocks
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks
import wagtailmedia.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("work", "0027_call_to_action"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "h2",
                        wagtail.blocks.CharBlock(
                            form_classname="title",
                            icon="title",
                            template="patterns/molecules/streamfield/blocks/heading2_block.html",
                        ),
                    ),
                    (
                        "h3",
                        wagtail.blocks.CharBlock(
                            form_classname="title",
                            icon="title",
                            template="patterns/molecules/streamfield/blocks/heading3_block.html",
                        ),
                    ),
                    (
                        "h4",
                        wagtail.blocks.CharBlock(
                            form_classname="title",
                            icon="title",
                            template="patterns/molecules/streamfield/blocks/heading4_block.html",
                        ),
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
                            template="patterns/molecules/streamfield/blocks/aligned_image_block.html",
                        ),
                    ),
                    (
                        "wide_image",
                        wagtail.blocks.StructBlock(
                            [("image", wagtail.images.blocks.ImageChooserBlock())],
                            label="Wide image",
                            template="patterns/molecules/streamfield/blocks/wide_image_block.html",
                        ),
                    ),
                    (
                        "bustout",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("text", wagtail.blocks.RichTextBlock()),
                            ],
                            template="patterns/molecules/streamfield/blocks/bustout_block.html",
                        ),
                    ),
                    (
                        "pullquote",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "quote",
                                    wagtail.blocks.CharBlock(
                                        form_classname="quote title"
                                    ),
                                ),
                                ("attribution", wagtail.blocks.CharBlock()),
                            ],
                            template="patterns/molecules/streamfield/blocks/pullquote_block.html",
                        ),
                    ),
                    (
                        "raw_html",
                        wagtail.blocks.RawHTMLBlock(
                            icon="code",
                            label="Raw HTML",
                            template="patterns/molecules/streamfield/blocks/raw_html_block.html",
                        ),
                    ),
                    (
                        "markdown",
                        wagtailmarkdown.blocks.MarkdownBlock(
                            icon="code",
                            template="patterns/molecules/streamfield/blocks/markdown_block.html",
                        ),
                    ),
                    (
                        "embed",
                        wagtail.embeds.blocks.EmbedBlock(
                            group="Media",
                            icon="code",
                            template="patterns/molecules/streamfield/blocks/embed_block.html",
                        ),
                    ),
                    (
                        "video_block",
                        wagtail.blocks.StructBlock(
                            [
                                ("video", wagtailmedia.blocks.VideoChooserBlock()),
                                (
                                    "autoplay",
                                    wagtail.blocks.BooleanBlock(
                                        default=False,
                                        help_text="Automatically start and loop the video. Please use sparingly.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "use_original_width",
                                    wagtail.blocks.BooleanBlock(
                                        default=False,
                                        help_text="Use the original width of the video instead of the default content width. Note that videos wider than the content width will be limited to the content width.",
                                        required=False,
                                    ),
                                ),
                            ],
                            group="Media",
                        ),
                    ),
                    (
                        "story_embed",
                        tbx.core.blocks.ExternalStoryEmbedBlock(
                            icon="code",
                            template="patterns/molecules/streamfield/blocks/external_story_block.html",
                        ),
                    ),
                ],
                use_json_field=True,
            ),
        ),
    ]
