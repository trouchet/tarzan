"""
Module: periodic_migrations.py

This module defines a custom Django management command for running 
database migrations periodically.

Custom Management Command:
    - Command: Run database migrations periodically.

"""

from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    """
    Command Class

    Custom management command for running database migrations periodically.

    Attributes:
        help (str): A brief description of the command for the user.

    """

    help = 'Run database migrations periodically'

    def handle(self, *args, **options):
        """
        Handle Method

        The main logic of the management command. Calls the 'migrate' management 
        command to run database migrations.

        Args:
            args: Positional arguments.
            options: Keyword arguments.

        """
        call_command('migrate')
