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
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField, AbstractFormField


class HomePage(Page):
    name = models.CharField(blank=True, max_length=25)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('name'),
            InlinePanel('role_titles', panels=None, heading='roles',
                        label='role_titles', min_num=1, max_num=4)], heading="landing info "),
    ]


class Roles(models.Model):
    page = ParentalKey(HomePage, on_delete=models.CASCADE,
                       related_name='role_titles')
    role = models.CharField(max_length=25)

    panels = [
        FieldPanel('role'),
    ]


class AboutPage(Page):
    resume = models.ForeignKey(
        'wagtaildocs.Document', blank=True, null=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    fun_fact = ParentalManyToManyField('home.FunFact', blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        MultiFieldPanel([
            DocumentChooserPanel('resume'),
            InlinePanel('related_links')], heading='Discovery Items'
        ),
        InlinePanel('knowledge_base', panels=None, heading='knowledge base',
                    label='skill', min_num=1, max_num=8),
        MultiFieldPanel([
            FieldRowPanel([
                MultiFieldPanel([
                    InlinePanel('left_highlight', min_num=1, max_num=1),
                    InlinePanel('left_highlight_bullet', panels=None, heading='bullets',
                                label='bullet', min_num=1, max_num=4)
                ]),
                MultiFieldPanel([
                    InlinePanel('right_highlight', min_num=1, max_num=1),
                    InlinePanel('right_highlight_bullet', panels=None, heading='bullets',
                                label='bullet', min_num=1, max_num=4),
                ], heading='right highlights'),
            ]),
        ], heading="Highlights Section"),
        FieldPanel('fun_fact', widget=forms.CheckboxSelectMultiple),
    ]


class AboutPageRelatedLink(Orderable):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE,
                       related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()
    icon = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
        ImageChooserPanel('icon'),
    ]


class KnowledgeBase(models.Model):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE,
                       related_name='knowledge_base')
    skill = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    icon = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL,
                             related_name='+', null=True
                             )

    panels = [
        FieldPanel('skill'),
        FieldPanel('description'),
        ImageChooserPanel('icon'),
    ]


class LeftBullet(models.Model):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE,
                       related_name='left_highlight_bullet')
    bullet = models.CharField(max_length=100)

    panels = [
        FieldPanel('bullet')
    ]


class RightBullet(models.Model):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE,
                       related_name='right_highlight_bullet')
    bullet = models.CharField(max_length=100)

    panels = [
        FieldPanel('bullet')
    ]


class LeftHighlight(models.Model):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE,
                       related_name='left_highlight')
    title = models.CharField(max_length=25)
    icon = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True)

    panels = [
        ImageChooserPanel('icon'),
        FieldPanel('title'),

    ]


class RightHighlight(models.Model):
    page = ParentalKey(AboutPage, on_delete=models.CASCADE,
                       related_name='right_highlight')
    title = models.CharField(max_length=25)
    icon = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+', null=True)

    panels = [
        ImageChooserPanel('icon'),
        FieldPanel('title'),

    ]


@register_snippet
class FunFact(models.Model):
    fact = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('fact'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.fact

    class Meta:
        verbose_name_plural = 'fun facts'


class ContactPage(AbstractEmailForm):
    location = models.CharField(max_length=50, blank=True)
    email_address = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(
        max_length=20, blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel([
                FieldPanel('location'),
                FieldPanel('email_address', heading='email address'),
                FieldPanel('phone_number', heading='phone number'),
            ], heading='contact page information'),
        InlinePanel('custom_form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Notification Config"),


    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()


class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='custom_form_fields')
