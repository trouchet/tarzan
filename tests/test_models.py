"""
This module contains a test for the string representation method of the Post model.

The Post model is assumed to be defined in the 'src.models' module. The test
checks whether the string representation of a Post object matches its title.

Usage:
    To run this test, call the 'test_post_model_str_method' function.

Example:
    test_post_model_str_method()  # Runs the test for the Post model's string representation.
"""

from tests.factories import PostFactory

def test_post_model_str_method():
    """
    Test the string representation method of the Post model.

    Creates a sample Post object using the factory and checks if its
    string representation matches the post title.

    Raises:
        AssertionError: If the string representation doesn't match the title.
    """
    # Create a sample post using the factory
    post = PostFactory()

    # Check if the string representation matches the title
    assert str(post) == post.title
