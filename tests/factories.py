# pylint: disable=R0903,C0115
"""
Module Docstring:

This module defines Factory class for necessary abstract concepts on the application.

"""

import factory
from django.utils import timezone
from src.models import Post


class PostFactory(factory.Factory):
    """
    Factory class for creating instances of the 'Post' model.

    This factory class allows you to create 'Post' model instances with default
    or customized values for attributes such as 'title', 'content', and 'pub_date'.

    Attributes:
        title (str): The title of the post.
        content (str): The content of the post.
        pub_date (datetime): The publication date and time of the post.

    Usage:
        To create a 'Post' instance with custom attributes:
        >>> post = PostFactory(title='Custom Title', content='Custom Content')

    """

    class Meta:
        model = Post

    title = 'Test Post Title'
    content = 'Test Post Content'
    pub_date = factory.LazyFunction(timezone.now)
