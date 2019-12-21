import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone

# 0 id; 1 name; 2 image; 3 price; 4 release_date; 5 lte_exists
# 1;Samsung Galaxy Edge 2;https://avatars.mds.yandex.net/get-mpic/364668/img_id5636027222104023144.jpeg/orig;73000;2016-12-12;True;

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # print(line)
                phone = Phone.objects.create(
                    id=line[0],
                    name=line[1],
                    price=line[3],
                    image=line[2],
                    release_date=line[4],
                    lte_exists=line[5],
                    slug=slugify(line[1])
                )


                # TODO: Добавьте сохранение модели pass
