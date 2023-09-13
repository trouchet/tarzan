"""
Module: models.py

This module defines the Post model for storing blog posts in the Django application.

The Post model includes fields for the title of the post, its content, and the publication date.

Classes:
    - Post: Represents a blog post with title, content, and publication date.

"""
from django.db.models import Model
from django.db.models import CharField, TextField, DateTimeField


class Post(Model):
    """
    Post Model

    Represents a blog post with a title, content, and publication date.

    Fields:
        title (CharField): The title of the blog post, limited to 200 characters.
        content (TextField): The content of the blog post, allowing for larger text.
        pub_date (DateTimeField): The date and time when the blog post was published.

    Methods:
        __str__: Returns a string representation of the post, which is its title.

    """

    title = CharField(max_length=200)
    content = TextField()
    pub_date = DateTimeField("date published")

    def __str__(self):
        return str(self.title)
