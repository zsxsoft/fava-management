from child import fava_child
from contextlib import closing
import multiprocessing as mp

import socket
import sys
import argparse
import shlex
import threading
import string
import secrets
from time import sleep

def generate_secure_random_string(stringLength=10):
    """Generate a secure random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(password_characters) for i in range(stringLength))

def parse_fava_opts (s):
    parser = argparse.ArgumentParser(description='Fava opts')
    parser.add_argument('filenames', nargs='*', help='filenames')
    parser.add_argument('--incognito', type=bool, default=False, nargs='?', const=True)
    return parser.parse_args(s)

def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]

class SingletonMixin(object):
	__singleton_lock = threading.Lock()
	__singleton_instance = None

	@classmethod
	def instance(cls):
		if not cls.__singleton_instance:
			with cls.__singleton_lock:
				if not cls.__singleton_instance:
					cls.__singleton_instance = cls()
		return cls.__singleton_instance

class FavaProcess (SingletonMixin):
    def __init__(self):
        super()
        fava_option = []
        arg = ''
        for arg in sys.argv:
            if arg[:7] == '--fava=':
                fava_option += shlex.split(arg[7:])
        self.fava_option = fava_option
        self.create_process()

    def create_process(self):
        self.port = find_free_port()
        self.key =generate_secure_random_string(10)
        fava_opts = vars(parse_fava_opts(self.fava_option))
        fava_opts['port'] = self.port
        fava_opts['key'] = self.key
        #ctx = mp.get_context('spawn')
        self.process = mp.Process(target=fava_child, args=[fava_opts])
        self.process.start()

    def restart(self):
        self.process.terminate()
        self.create_process()
