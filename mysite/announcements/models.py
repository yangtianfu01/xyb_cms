from django.db import models

# Create your models here.
from wagtail.core.models import Page 
from wagtail.core.fields import RichTextField 
from wagtail.admin.edit_handlers import FieldPanel 
from wagtail.search import index 
from wagtail.api import APIField # api导出字段模块
from wagtail.core.templatetags import wagtailcore_tags

class AnnouncementIndexPage(Page):
	def get_context(self, request):
		context = super().get_context(request)
		anncpages = self.get_children().live().order_by('-first_published_at')
		context['anncpages'] = anncpages
		return context

class AnnouncementPage(Page):
	annc_title = models.CharField(max_length=250, verbose_name='公告标题')
	date = models.DateField("发布时间")
	body = RichTextField(blank=True) # 正文

	content_panels = Page.content_panels + [
		FieldPanel('annc_title'),
		FieldPanel('date'),
		FieldPanel('body'),
	]

	def rendered_body(self):
		return wagtailcore_tags.richtext(self.body)

	api_fields = [
		APIField('annc_title'),
		APIField('date'),
		APIField('rendered_body'),
	]


