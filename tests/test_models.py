import pytest
from django.utils import timezone
from src.models import Post

def test_post_model_str_method():
    # Create a sample post
    post_title = "Test Post Title"
    post = Post(title=post_title, content="Test Post Content", pub_date=timezone.now())

    # Check if the string representation matches the title
    assert str(post) == post_title