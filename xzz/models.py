# coding: utf-8
# Есть такой код. Сделайте что-нибудь с Item.get_options().

from django.db import models
from typing import Dict, Tuple


class Item(models.Model):
	# .....

	def get_options(self):
		values_map: Dict[Tuple[int, int], ItemOption] = {}
		for d in self.itemoption_set.values('item__pk', 'option__pk', 'value'):
			values_map[(d['item__pk'], d['option__pk'])] = d['value']

		for topic in Topic.objects.all().prefetch_related('option_set'):
			options = []
			for option in topic.option_set.all():
				options.append({
					'title': option.title,
					'value': values_map.get((self.pk, option.pk), None)
				})
			yield {'name': topic.name, 'options': options}


class Topic(models.Model):
	name = models.CharField(max_length=255)


class Option(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)


class ItemOption(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	option = models.ForeignKey(Option, on_delete=models.CASCADE)
	value = models.CharField(max_length=20)
