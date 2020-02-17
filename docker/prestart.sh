#!/bin/sh
python manage.py migrate
echo "from django.contrib.auth.models import User;User.objects.create_superuser(username='${USERNAME}', password='${PASSWORD}', email='${USERNAME}')" | python manage.py shell
export PASSWORD=
