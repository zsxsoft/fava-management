"""The command-line interface for Fava."""

import os
import errno
import click

from werkzeug.middleware.profiler import ProfilerMiddleware
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from cheroot import wsgi

from fava.application import app
from fava.util import simple_wsgi
from fava import __version__
from werkzeug.wrappers import Request, Response, ResponseStream

class CheckKeyMiddleware():
    def __init__(self, app, key):
        self.app = app
        self.key = key

    def __call__(self, environ, start_response):
        request = Request(environ)
        requestKey = request.headers.get('key', '')
        if requestKey == self.key:
            return self.app(environ, start_response)
        res = Response(u'Authorization failed', mimetype= 'text/plain', status=401)
        return res(environ, start_response)

def fava_child(args):
    filenames = args['filenames']
    port = args['port']
    incognito = args['incognito']
    key = args['key']
    host = '127.0.0.1'
    port = port
    prefix = '/fava'

    env_filename = os.environ.get("BEANCOUNT_FILE")
    if env_filename:
        filenames = filenames + tuple(env_filename.split())

    if not filenames:
        raise click.UsageError("No file specified")

    app.config["BEANCOUNT_FILES"] = filenames
    app.config["INCOGNITO"] = incognito

    if prefix:
        app.wsgi_app = DispatcherMiddleware(
            simple_wsgi, {prefix: app.wsgi_app}
        )
    app.wsgi_app = CheckKeyMiddleware(app.wsgi_app, key)

    server = wsgi.Server((host, port), app)
    print("Running Fava on http://{}:{}".format(host, port))
    server.safe_start()
