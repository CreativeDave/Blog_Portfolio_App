from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet


class ProjectIndexPage(Page):
    intro = RichTextField(blank=True)
    categories = ParentalManyToManyField('project.ProjectCategory', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('index_gallery_images', label="Main Page Image"),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]

    def main_image(self):
        gallery_item = self.index_gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        projectpages = self.get_children().live()
        context['projectpages'] = projectpages
        return context


class ProjectPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=300)
    outcome = RichTextField(blank=True)
    description = RichTextField(blank=True)
    categories = ParentalManyToManyField('project.ProjectCategory', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def related_link(self):
        gallery_link = self.related_links.first()
        if gallery_link:
            return gallery_link.url
        else:
            return None

    def related_link_name(self):
        gallery_link = self.related_links.first()
        if gallery_link:
            return gallery_link.name
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('description'),
        index.SearchField('outcome'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
        ], heading="Project information"),
        FieldPanel('intro'),
        FieldPanel('outcome'),
        FieldPanel('description'),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        InlinePanel('related_links', label="Related links"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        projectsections = self.get_children().live()
        context['projectsections'] = projectsections
        return context


class ProjectPageRelatedLink(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.CASCADE,
                       related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]


class ProjectPageGalleryImage(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.CASCADE,
                       related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class ProjectIndexPageGalleryImage(Orderable):
    page = ParentalKey(ProjectIndexPage, on_delete=models.CASCADE,
                       related_name='index_gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


@register_snippet
class ProjectCategory(models.Model):
    name = models.CharField(max_length=25)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'project categories'
