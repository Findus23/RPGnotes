#!/bin/bash
set -x
set -e

python="/srv/venv/rpgnotes/bin/python"

manage="sudo -u rpgnotes $python manage.py"

git pull

$manage scss
npm run build
$manage collectstatic --noinput
$manage migrate
$manage clearcache
$manage clearsessions
$manage thumbnail clear_delete_referenced

sudo systemctl reload rpgnotes.service
