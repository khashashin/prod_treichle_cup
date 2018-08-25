# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(on_delete=models.CASCADE, parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('tournament_section_title', models.CharField(blank=True, help_text='Title to display above the next matches', max_length=255, null=True)),
                ('matches_section_title', models.CharField(blank=True, help_text='Title to display above the next matches', max_length=255, null=True)),
                ('news_section_title', models.CharField(blank=True, help_text='Title to display above the News section on Home page', max_length=255, null=True)),
                ('presentation_screen_section_title', models.CharField(blank=True, help_text='Title to display above the News section on Home page', max_length=255, null=True)),
                ('matches_section', models.ForeignKey(blank=True, help_text='Choose a page to link to for the Matches Page', null=True, on_delete=models.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Choose ')),
                ('news_section', models.ForeignKey(blank=True, help_text='Choose a page to link to for the News Page.', null=True, on_delete=models.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='News')),
                ('presentation_screen_section', models.ForeignKey(blank=True, help_text='Choose a page to link to for the Presentation Screen Page.', null=True, on_delete=models.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Presentation Screen')),
                ('tournament_section', models.ForeignKey(blank=True, help_text='Choose a page to link to for the Matches Page', null=True, on_delete=models.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Choose ')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
