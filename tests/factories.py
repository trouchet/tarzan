import factory
from django.utils import timezone
from src.models import Post

class PostFactory(factory.Factory):
    class Meta:
        model = Post

    title = 'Test Post Title'
    content = 'Test Post Content'
    pub_date = factory.LazyFunction(timezone.now)