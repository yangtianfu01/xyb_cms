from django.db import models

# Create your models here.
from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField 
from wagtail.admin.edit_handlers import FieldPanel 
from wagtail.api import APIField # api导出字段模块

class LinksIndexPage(Page):
	pass

class LinksPage(Page):
	links_name = models.CharField(max_length=250, verbose_name='友链名称')
	links_url = models.CharField(max_length=250, verbose_name='友链地址')

	content_panels = Page.content_panels + [
		FieldPanel('links_name'),
		FieldPanel('links_url'),
	]

	api_fields = [
		APIField('links_name'),
		APIField('links_url'),
	]