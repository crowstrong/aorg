#!/bin/ash

echo "Starting Celery"
exec celery -A config worker -l ${CELERY_LOG_LEVEL} -c ${CELERY_NUM_WORKERS}