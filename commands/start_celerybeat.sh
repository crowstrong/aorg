#!/bin/ash

echo "Starting Celery Beat"
exec celery -A config worker -l ${CELERY_LOG_LEVEL} -S django

