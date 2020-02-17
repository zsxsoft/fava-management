from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from revproxy.views import ProxyView
from proxy.process import FavaProcess

from child import fava_child
from contextlib import closing
from multiprocessing import Process

import socket
import sys
import argparse
import shlex
import logging
from time import sleep


# too noisy...
logging.getLogger('revproxy.view').setLevel(logging.ERROR)
logging.getLogger('revproxy.response').setLevel(logging.ERROR)

@method_decorator(login_required(login_url = '/'), 'dispatch')
class ReverseFava(ProxyView):
    def __init__(self):
        super().__init__()
        process = FavaProcess.instance()
        self.upstream = 'http://127.0.0.1:' + str(process.port) + '/fava/'

@login_required(login_url = '/')
def restart(request):
    process = FavaProcess.instance()
    process.restart()
    return HttpResponse("done")
