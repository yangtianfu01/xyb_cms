from django.db import models

# Create your models here.
from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField 
from wagtail.admin.edit_handlers import FieldPanel 
from wagtail.api import APIField # api导出字段模块
from wagtail.core.templatetags import wagtailcore_tags

class ContactPage(Page):
	body = RichTextField(blank=True) # 正文
	content_panels = Page.content_panels + [
		FieldPanel('body'),
	]

	def rendered_body(self):
		return wagtailcore_tags.richtext(self.body)

	api_fields = [
		APIField('rendered_body'),
	]