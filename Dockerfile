FROM python:3.13-alpine
COPY --from=astral/uv:0.9.21 /uv /uvx /bin/

WORKDIR /app
ENV BEANCOUNT_FILE /bean/main.bean
COPY uv.lock pyproject.toml /app/

RUN apk add --update --no-cache  --virtual .build-deps flex bison gcc libc-dev libxml2-dev rust cargo python3-dev libxml2 libxslt-dev && \
    uv sync && \
    apk del .build-deps

RUN apk add openssh git && \
    mkdir /root/.ssh

COPY . /app
COPY docker/prestart.sh /app/prestart.sh
COPY docker/* /docker/
ENV PYTHONPATH /bean
ENV PATH /app/.venv/bin:$PATH
RUN yes | python3 manage.py collectstatic && \
    sed -i 's/DEBUG = True/DEBUG = False/g' management/settings.py

ENV WORKERS 4
ENTRYPOINT [ "/app/prestart.sh" ]
CMD ["gunicorn", "management.wsgi", "-w", "4", "-b", ":80"]
