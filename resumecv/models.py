from __future__ import absolute_import, unicode_literals
from django import forms
from django.db import models


from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.documents.edit_handlers import DocumentChooserPanel


class ResumePage(Page):
    heading = models.CharField(max_length=20, blank=True)
    TechnicalSkills = ParentalManyToManyField(
        'resumecv.TechnicalSkills', blank=True)
    PersonalSkills = ParentalManyToManyField(
        'resumecv.PersonalSkills', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('heading', classname="full"),
        MultiFieldPanel([
                InlinePanel('experience_item', heading='experience',
                            label='experience item', min_num=1, max_num=5),
                InlinePanel('education_item', heading='education',
                            label='education item', min_num=1, max_num=5),
        ], heading='Experience/Education'),
        FieldPanel('TechnicalSkills', widget=forms.CheckboxSelectMultiple),
        FieldPanel('PersonalSkills', widget=forms.CheckboxSelectMultiple),

    ]


class ExperienceSectionItem(models.Model):
    page = ParentalKey(ResumePage, on_delete=models.CASCADE,
                       related_name='experience_item')
    title = models.CharField(max_length=25)
    dates = models.CharField(max_length=50)
    company_location = models.CharField(max_length=250, blank=True)
    description = RichTextField(max_length=100, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('dates'),
        FieldPanel('company_location'),
        FieldPanel('description'),
    ]


class EducationSectionItem(models.Model):
    page = ParentalKey(ResumePage, on_delete=models.CASCADE,
                       related_name='education_item')
    title = models.CharField(max_length=25)
    dates = models.CharField(max_length=50)
    company_location = models.CharField(max_length=250, blank=True)
    description = RichTextField(max_length=100, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('dates'),
        FieldPanel('company_location'),
        FieldPanel('description'),
    ]


@register_snippet
class TechnicalSkills(models.Model):
    name = models.CharField(max_length=25)
    percent = models.CharField(max_length=4, default='100%')

    panels = [
        FieldPanel('name'),
        FieldPanel('percent'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'technical skills percentages'


@register_snippet
class PersonalSkills(models.Model):
    name = models.CharField(max_length=25)
    percent = models.CharField(max_length=4, default='100%')

    panels = [
        FieldPanel('name'),
        FieldPanel('percent'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'personal skills percentages'
