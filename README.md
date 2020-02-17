fava-management
===========================

A fava management panel.

If you want to deploy fava on the server, you will find that the fava process may crash frequently. This project is a fava controller that allows you to restart fava in your browser. In addition, this project also added Django-based authentication to Fava.

## Features
1. Fava restart
2. Fava authentication

## Installation
```bash
git clone https://github.com/zsxsoft/fava-management
cd fava-management
# If you have your own fava and beancount installed, you can just
# pip install django django-revproxy
pip install -r requirements.txt
# Create database
python manage.py migrate
# Create superuser
python manage.py createsuperuser
```

## Development
```bash
python3 manage.py runserver --fava="your_beancount_entrypoint_file"
```

See [Django documentation](https://docs.djangoproject.com/en/3.0/ref/django-admin/) for details.

## Production
You need to setup static files, otherwise your CSS may not work properly. BTW it's not important, fava always works fine.

```bash
BEANCOUNT_FILE=your_beancount_entrypoint_file gunicorn management.wsgi
```
See [Gunicorn documentation](https://docs.gunicorn.org/en/latest/run.html#django) for details.

## Need more security?

Try them:

- [https://github.com/sdonk/django-admin-ip-restrictor/](https://github.com/sdonk/django-admin-ip-restrictor/)
- [https://github.com/django-otp/django-otp](https://github.com/django-otp/django-otp)
- [https://github.com/volrath/django-captcha-admin](https://github.com/volrath/django-captcha-admin)

## License
The MIT License
