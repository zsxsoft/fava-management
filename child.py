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

def fava_child(args):
    filenames = args['filenames']
    port = args['port']
    incognito = args['incognito']
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

    server = wsgi.Server((host, port), app)
    print("Running Fava on http://{}:{}".format(host, port))
    server.safe_start()

#fava_child()
