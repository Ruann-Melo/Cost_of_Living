import scrapy
from unidecode import unidecode
# noinspection PyUnresolvedReferences
from cost_of_living.items import HousingItem


class PlacesSpider(scrapy.Spider):
    name = 'housing'
    start_urls = [
        'https://www.vivareal.com.br/aluguel/pernambuco/recife/?pagina=200'
    ]

    def parse(self, response, **kwargs):
        housing_item = HousingItem()

        for place in response.css('a.property-card__content-link'):
            housing_item['headline'] = unidecode(place.css('span.property-card__title::text').get()),
            housing_item['price'] = place.css('div.property-card__price p::text').get(),
            housing_item['period'] = place.css('span.property-card__price-period::text').get(),
            housing_item['address'] = unidecode(place.css('span.property-card__address::text').get()),
            housing_item['area'] = unidecode(place.css(
                'span.property-card__detail-area::text').get() + place.css(
                'li.property-card__detail-item span.property-card__detail-text::text').get()),
            housing_item['rooms'] = place.css(
                'li.property-card__detail-room span.property-card__detail-value::text').get() + place.css(
                'li.property-card__detail-room span.property-card__detail-text::text').get(),
            housing_item['bathrooms'] = place.css(
                'li.property-card__detail-bathroom span.property-card__detail-value::text').get() + place.css(
                'li.property-card__detail-bathroom span.property-card__detail-text::text').get(),
            housing_item['garage'] = place.css(
                'li.property-card__detail-garage span.property-card__detail-value::text').get() + place.css(
                'li.property-card__detail-garage span.property-card__detail-text::text').get(),
            housing_item['link'] = 'https://www.vivareal.com.br' + place.css('a.property-card__content-link::attr(href)').get(),
            housing_item['city'] = 'Recife'

            yield housing_item

        next_page = response.xpath('//button[@title="Próxima página"]/@data-page').get()
        if next_page is not '':
            yield response.follow(
                'https://www.vivareal.com.br/aluguel/pernambuco/recife/?pagina=' + next_page
                , callback=self.parse
            )
