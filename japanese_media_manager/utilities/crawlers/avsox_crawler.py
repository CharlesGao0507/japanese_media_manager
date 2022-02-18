import re
import io
import datetime
import PIL.Image

from .base import Base

class TAG:
    NUMBER = '识别码:'
    RELEASE_DATE = '发行时间:'
    LENGTH = '长度:'
    STUDIO = '制作商:'
    KEYWORDS = '类别:'
    SERIES = '系列:'

class AvsoxCrawler(Base):
    def __init__(self, *args, base_url='https://avsox.monster', **kwargs):
        self.base_url = base_url
        super().__init__(*args, **kwargs)

    def get_page_soup(self, number):
        response = self.get(f'{self.base_url}/cn/search/{number.upper()}')

        soup = self.get_soup(response.text)
        for tag in soup.find_all('div', 'item'):
            for link in tag.find_all('a'):
                if number.upper() in link.text.upper():
                    response = self.get(f'https:{link.attrs["href"]}')
                    return self.get_soup(response.text)
        return self.get_soup('')

    def get_poster(self, soup):
        return None

    def get_fanart(self, soup):
        for tag in soup.find_all('a', 'bigImage'):
            response = self.get(tag.attrs['href'])
            return PIL.Image.open(io.BytesIO(response.content))
        return None

    def get_keywords(self, soup):
        keywords = []
        for tag in soup.find_all('p', 'header'):
            if not tag.text == TAG.KEYWORDS:
                continue
            for item in tag.find_next('span'):
                keywords.append(item.text)
        return keywords

    def get_series(self, soup):
        for tag in soup.find_all('p', 'header'):
            if tag.text == TAG.SERIES:
                return tag.find_next('p').text
        return None

    def get_number(self, soup):
        for tag in soup.find_all('span', 'header'):
            if tag.text == TAG.NUMBER:
                _, number_tag = tag.parent.find_all('span')
                return number_tag.text
        return None

    def get_release_date(self, soup):
        for tag in soup.find_all('span', 'header'):
            if tag.text == TAG.RELEASE_DATE:
                return datetime.datetime.strptime(tag.next.next.strip(), '%Y-%m-%d').date()
        return None

    def get_length(self, soup):
        for tag in soup.find_all('span', 'header'):
            if tag.text == TAG.LENGTH:
                match = re.match(pattern=r'(?P<number>\d+)(?P<unit>\w+)', string=tag.next.next.strip())
                if match:
                    return match.groupdict()['number'], match.groupdict()['unit']
        return None

    def get_stars(self, soup):
        stars = []
        for tag in soup.find_all('div', attrs={'id': 'avatar-waterfall'}):
            for item in tag.find_all('a', 'avatar-box'):
                stars.append(
                    {
                        'avatar_url': item.find_next('img').attrs['src'],
                        'name': item.find_next('span').text
                    }
                )
        return stars

    def get_studio(self, soup):
        for tag in soup.find_all('p', 'header'):
            if tag.text.strip() == TAG.STUDIO:
                return tag.find_next('p').text
        return None

    def get_title(self, soup):
        for tag in soup.find_all('h3'):
            return tag.text
        return None

    def get_director(self, soup):
        return None

    def get_outline(self, soup):
        return None