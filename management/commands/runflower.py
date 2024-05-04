from django.core.management.base import BaseCommand
from flower.command import FlowerCommand


class Command(BaseCommand):
    help = "Starts Flower monitoring tool"

    def handle(self, *args, **options):
        flower = FlowerCommand()
        flower.execute_from_commandline(["", "--port=5555"])
