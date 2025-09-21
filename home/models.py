from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel

class FlexPage(Page):
    body = StreamField(
        [
            ("heading", blocks.CharBlock(form_classname="title")),
            ("paragraph", blocks.RichTextBlock(features=["bold","italic","ol","ul","link"])),
            ("image", ImageChooserBlock()),
            ("cta", blocks.StructBlock({
                "text": blocks.CharBlock(),
                "url": blocks.URLBlock(),
            })),
        ],
        use_json_field=True, blank=True,
    )

    content_panels = Page.content_panels + [FieldPanel("body")]