from django.db import models

# Create your models here.
from wagtail.core.models import Page, Orderable 
from wagtail.core.fields import RichTextField 
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel # 组件间集成

from modelcluster.fields import ParentalKey # 图片索引
from wagtail.images.edit_handlers import ImageChooserPanel # 图片选择UI

from wagtail.search import index 
from wagtail.api import APIField # api导出字段模块


class GalleryIndexPage(Page):
	pass

class GalleryPage(Page):
	intro = models.CharField(max_length=250, verbose_name='轮播图链接')
	feed_image = models.ForeignKey('wagtailimages.Image', on_delete=models.SET_NULL, null=True)

	content_panels = Page.content_panels + [
		FieldPanel('intro'),
		ImageChooserPanel('feed_image'),
		InlinePanel('gallery_img', label='轮播图'),
	]

	api_fields = [
		APIField('intro'),
		APIField('feed_image'),
	]


class GalleryImage(Orderable):
	page = ParentalKey(GalleryPage, on_delete=models.CASCADE, related_name='gallery_img')
	image = models.ForeignKey(
		'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', verbose_name='选择图片') 
	caption = models.CharField(blank=True, max_length=250, verbose_name='图片标题')

	panels = [
		ImageChooserPanel('image'),
		FieldPanel('caption'),
	]
