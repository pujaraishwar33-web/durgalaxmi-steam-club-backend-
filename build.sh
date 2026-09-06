#!/usr/bin/env bash
# Render build script
set -o errexit

python manage.py collectstatic --no-input
python manage.py migrate