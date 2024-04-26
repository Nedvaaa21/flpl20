from random import randint
from django.core.management.base import BaseCommand, CommandError
from main.models import Soft
from faker import Faker



class Command(BaseCommand):
    help = 'Генерація нових фейкових книг'

    def add_arguments(self, parser):
        parser.add_argument('total',type=int,help='Кількість книг для додавання')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            b = Faker()
            try:
                Soft.objects.create(
                    title = b.company(),
                    author = b.name(),
                    text = ' '.join(b.sentences(4)),
                    published = str(b.year()),
                    count = randint(1, 20)
                )
            except:
                raise CommandError('Generation ERROR')
            else:
                print(f'{i+1} книг додалось!')