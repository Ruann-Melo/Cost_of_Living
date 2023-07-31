# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CostOfLivingPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        value = ''.join(map(str, adapter.get('price')))
        value = value.strip().replace('R$', '')
        adapter['price'] = value

        return item
