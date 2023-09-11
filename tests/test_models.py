"""
This module contains a test for the string representation method of the Post model.

The Post model is assumed to be defined in the 'src.models' module. The test
checks whether the string representation of a Post object matches its title.

Usage:
    To run this test, call the 'test_post_model_str_method' function.

Example:
    test_post_model_str_method()  # Runs the test for the Post model's string representation.
"""

from django.utils import timezone
from src.models import Post

def test_post_model_str_method():
    """
    Test the string representation method of the Post model.

    Creates a sample Post object and checks if its string representation
    matches the post title.

    Raises:
        AssertionError: If the string representation doesn't match the title.
    """
    # Create a sample post
    post_title = 'Test Post Title'
    post = Post(title=post_title, content='Test Post Content', pub_date=timezone.now())

    # Check if the string representation matches the title
    assert str(post) == post_title
