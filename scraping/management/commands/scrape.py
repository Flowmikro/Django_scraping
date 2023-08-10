from django.core.management.base import BaseCommand

from urllib.request import urlopen
from bs4 import BeautifulSoup
from scraping.models import Job


class Command(BaseCommand):
    help = "collect jobs"

    # определяем логику команд
    def handle(self, *args, **options):

        # собираем html
        html = urlopen('https://jobs.lever.co/opencare')

        # преобразуем в soup-объект
        soup = BeautifulSoup(html, 'html.parser')

        # собираем все посты
        postings = soup.find_all("div", class_="posting")
        print(postings)
        for p in postings:
            url = p.find('a', class_='posting-btn-submit')['href']
            title = p.find('h5').text
            try:
                # сохраняем в базе данных
                Job.objects.create(
                    url=url,
                    title=title,)
            except:
                print('ВСЕ' % (title,))

        self.stdout.write( 'job complete' )