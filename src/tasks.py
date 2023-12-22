"""
Module Description

This module contains a Celery shared task for background processing.

It defines a Celery shared task called `my_task` that can be used for performing
background processing. The task takes two arguments, arg1 and arg2, and returns
a tuple containing these arguments after performing some background task logic.
"""

from celery import shared_task


@shared_task
def my_task(arg1, arg2):
    """
    This function defines a Celery shared task for background processing.

    Args:
        arg1: The first argument for the task.
        arg2: The second argument for the task.

    Returns:
        tuple: A tuple containing arg1 and arg2.

    This function can be used as a Celery task to perform background processing.
    It takes two arguments, arg1 and arg2, and returns a tuple containing these
    arguments after performing some background task logic.
    """

    # Your background task logic here
    return arg1, arg2
