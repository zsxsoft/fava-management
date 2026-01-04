fava-management
===========================

A fava management panel.

If you want to deploy fava on the server, you will find that the fava process may crash frequently. This project is a fava controller that allows you to restart fava in your browser. In addition, this project also added Django-based authentication to Fava.

## Features
1. Fava restart
2. Fava authentication

## Installation

Recommended installation method is using [uv](https://github.com/astral-sh/uv).

```bash
git clone https://github.com/zsxsoft/fava-management
cd fava-management
uv sync
# Create database
uv run manage.py migrate
# Create superuser
uv run manage.py createsuperuser
```

## Development
```bash
uv run manage.py runserver --fava="your_beancount_entrypoint_file"
```

See [Django documentation](https://docs.djangoproject.com/en/6.0/ref/django-admin/) for details.

## Production
```bash
BEANCOUNT_FILE=your_beancount_entrypoint_file gunicorn management.wsgi
```
See [Gunicorn documentation](https://docs.gunicorn.org/en/latest/run.html#django) for details.

## Docker
```bash
docker run --rm -v/home/ubuntu/bean:/bean -p8080:80 -eBEANCOUNT_FILE=/bean/main.bean -eUSERNAME=admin -ePASSWORD=12345678 -it zsxsoft/fava-management
```

## Need more security?

Try them:

- [https://github.com/sdonk/django-admin-ip-restrictor/](https://github.com/sdonk/django-admin-ip-restrictor/)
- [https://github.com/django-otp/django-otp](https://github.com/django-otp/django-otp)
- [https://github.com/volrath/django-captcha-admin](https://github.com/volrath/django-captcha-admin)

## License
The MIT License
