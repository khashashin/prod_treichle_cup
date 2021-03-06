from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (
    FieldPanel,
    PageChooserPanel,
    MultiFieldPanel,
)

class HomePage(Page):
    # Tournaments List future for next version
    tournament_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the next matches'
    )
    tournament_section = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Choose ',
        help_text='Choose a page to link to for the Matches Page'
    )
    # Matches List future for next version
    matches_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the next matches'
    )
    matches_section = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Choose ',
        help_text='Choose a page to link to for the Matches Page'
    )

    news_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the News section on Home page'
    )
    news_section = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Choose a page to link to for the News Page.',
        verbose_name='News'
    )


    presentation_screen_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the News section on Home page'
    )
    presentation_screen_section = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Choose a page to link to for the Presentation Screen Page.',
        verbose_name='Presentation Screen'
    )
    parent_page_types = ['wagtailcore.Page']

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            MultiFieldPanel([
                FieldPanel('tournament_section_title'),
                PageChooserPanel('tournament_section'),
                ]),
            MultiFieldPanel([
                FieldPanel('matches_section_title'),
                PageChooserPanel('matches_section'),
                ]),
            MultiFieldPanel([
                FieldPanel('news_section_title'),
                PageChooserPanel('news_section'),
                ]),
            MultiFieldPanel([
                FieldPanel('presentation_screen_section_title'),
                PageChooserPanel('presentation_screen_section'),
                ]),
        ], heading="Featured homepage sections", classname="collapsible")
    ]

    def __str__(self):
        return self.title
