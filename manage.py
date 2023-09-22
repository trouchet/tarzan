#!/usr/bin/env python
# pylint: disable=C0415
"""
Django's command-line utility for administrative tasks.
"""
import sys
import os


# Add the project directory to sys.path
project_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_directory)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            'available on your PYTHONPATH environment variable? Did you '
            'forget to activate a virtual environment?'
        )
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
