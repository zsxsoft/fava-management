#!/usr/bin/env python
import os
import sys
import shlex
import argparse

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'management.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    argv = []
    for arg in sys.argv:
        if arg[:7] != '--fava=':
            argv.append(arg)
    execute_from_command_line(argv)


if __name__ == '__main__':
    main()
