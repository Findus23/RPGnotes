#!/bin/bash
set -x
set -e

python="/srv/venv/rpgnotes/bin/python"

manage="sudo -u rpgnotes $python manage.py"

git pull

$manage scss
$manage collectstatic --noinput
$manage migrate
$manage clearcache
$manage thumbnail clear_delete_referenced

sudo systemctl reload rpgnotes.service
