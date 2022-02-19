from re import match
from datetime import datetime, date
from io import BytesIO
from typing import List, Any, Tuple, Dict, Optional
from bs4 import BeautifulSoup
from PIL.Image import Image

from .base import Base

class TAG:
    RELEASE_DATE = '発売日：'
    LENGHT = '収録時間：'
    NUMBER = '品番：'
    DIRECTOR = '監督：'
    SERIES = 'AVレーベル：'
    STUDIO = 'AVメーカー：'
    STARTS = 'AV女優：'

class ArzonCrawler(Base):
    def __init__(self, *args: Any, base_url: str = 'https://www.arzon.jp', **kwargs: Any):
        self.base_url = base_url
        super().__init__(*args, **kwargs)
        self.get(f'{self.base_url}/index.php', params={'action': 'adult_customer_agecheck', 'agecheck': '1'})

    def get_page_soup(self, number: str) -> BeautifulSoup:
        params = {'mitemcd': number, 'd': 'all', 't': 'all', 's': 'all', 'm': 'all'}
        response = self.get(f'{self.base_url}/itemlist.html', params=params)
        response.encoding = 'utf8'
        soup = self.get_soup(response.text)

        for tag in soup.find_all('div', 'pictlist'):
            for link in tag.find_all('a'):
                response = self.get(f'{self.base_url}{link.attrs["href"]}')
                response.encoding = 'utf8'
                return self.get_soup(response.text)
        return self.get_soup('')

    def get_fanart(self, soup: BeautifulSoup) -> Optional[Image]:
        return None

    def get_poster(self, soup: BeautifulSoup) -> Optional[Image]:
        return None

    def get_keywords(self, soup: BeautifulSoup) -> List[str]:
        return []

    def get_title(self, soup: BeautifulSoup) -> Optional[str]:
        for tag in soup.find_all('h1'):
            return tag.text
        return None

    def get_release_date(self, soup: BeautifulSoup) -> Optional[date]:
        for tag in soup.find_all('td'):
            if not tag.text == TAG.RELEASE_DATE:
                continue

            result = match(pattern=r'(?P<date>\d+/\d+/\d+)', string=tag.find_next('td').text.strip())
            if not result:
                continue

            return datetime.strptime(result.groupdict()['date'], '%Y/%m/%d').date()
        return None

    def get_length(self, soup: BeautifulSoup) -> Optional[Tuple[int, str]]:
        for tag in soup.find_all('td'):
            if not tag.text == TAG.LENGHT:
                continue

            result = match(pattern=r'(?P<length>\d+)(?P<unit>\w+)', string=tag.find_next('td').text.strip())
            if not result:
                continue
            return (result.groupdict()['length'], result.groupdict()['unit'])
        return None

    def get_number(self, soup: BeautifulSoup) -> Optional[str]:
        return None

    def get_director(self, soup: BeautifulSoup) -> Optional[str]:
        for tag in soup.find_all('td'):
            if not tag.text == TAG.DIRECTOR:
                continue

            return tag.find_next('td').text.strip()
        return None

    def get_series(self, soup: BeautifulSoup) -> Optional[str]:
        for tag in soup.find_all('td'):
            if not tag.text == TAG.SERIES:
                continue

            return tag.find_next('td').text.strip()
        return None

    def get_studio(self, soup: BeautifulSoup) -> Optional[str]:
        for tag in soup.find_all('td'):
            if not tag.text == TAG.STUDIO:
                continue

            return tag.find_next('td').text.strip()
        return None

    def get_stars(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        stars = []
        for tag in soup.find_all('td'):
            if not tag.text == TAG.STARTS:
                continue

            for link in tag.find_next('td').find_all('a'):
                response = self.get(f'{self.base_url}{link.attrs["href"]}')
                response.encoding = 'utf8'
                soup = self.get_soup(response.text)

                for item in soup.find_all('table', 'p_list1'):
                    image = item.find_next('img')
                    stars.append(
                        {
                            'name': image.attrs['alt'],
                            'avatar_url': f'https:{image.attrs["src"]}'
                        }
                    )
        return stars

    def get_outline(self, soup: BeautifulSoup) -> Optional[str]:
        for tag in soup.find_all('h2'):
            return tag.next.next.strip()
        return None
