from django.contrib.auth.models import User
from django.core.management import BaseCommand, CommandError
from argparse import ArgumentParser


class Command(BaseCommand):

    def handle(self, *args, **options):
        activae = options['activateuser']
        User.is_active = True

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('activateuser', metavar='ACTIVE-USER', help='active user')


class Command1(BaseCommand):

    def handle(self, *args, **options):
        de_activae = options['activateuser']
        User.is_active = False

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('deactivateuserr', metavar='DE-ACTIVE-USER', help='de - active user')
