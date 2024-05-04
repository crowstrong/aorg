from celery import Celery
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Starts Celery worker"

    def handle(self, *args, **options):
        celery_app = Celery()
        celery_app.worker_main(["", "--loglevel=info"])
