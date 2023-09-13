To perform unit and integration testing in a Django project and set up a pre-configured testing environment, you can follow these steps:

**Create a Django Testing Environment**

Django provides a testing framework that allows you to create a separate database for testing purposes, ensuring that your tests don't affect your production database. Here's how to set up a pre-configured testing environment:

- Configure Test Database:

In your Django project's settings (settings.py), define a separate database configuration specifically for testing. This ensures that your tests won't modify your production database. Here's an example:

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Production database
    },
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'test_db.sqlite3',  # Test database
    },
}
```

- Use TestCase for Test Classes:

In your test classes, inherit from django.test.TestCase rather than the standard unittest.TestCase. The TestCase class provides utilities for setting up and tearing down the test database.

- Use Test Fixtures:

You can create fixtures (predefined data) to populate your test database with sample data. This can be helpful for testing scenarios with specific data requirements.

**Use pytest for Test Automation**

pytest is a popular testing framework that simplifies test writing and execution. Here's how to set up and use pytest for your Django project:

- Install pytest and Related Packages:

Install pytest and any necessary packages for Django testing:

```bash
pip install pytest pytest-django
```

- Create Test Files:

Organize your tests into separate Python files within a directory named tests in your Django app(s). For example:

```markdown
myapp/
    tests/
        test_models.py
        test_views.py
        ...
```

- Write Test Functions:

Write test functions using pytest conventions. Test function names should start with test_. Use the django.test.Client class to simulate HTTP requests in your tests.

```python
# test_views.py

from django.test import Client
import pytest

@pytest.mark.django_db
def test_my_view():
    client = Client()
    response = client.get('/my-url/')
    assert response.status_code == 200
```

- Run Tests with pytest:

Execute your tests using the pytest command:

```bash
pytest
```

pytest will automatically discover and run your tests in the tests directory.

**Use Test Fixtures (Optional)**

You can create fixtures to set up predefined data for your tests. Fixtures are defined in Python files with the .py extension and are typically stored in a fixtures directory within your app.

For example, you can create a sample_data.json fixture file with predefined data:

```json
// sample_data.json

[
    {
        "model": "myapp.mymodel",
        "pk": 1,
        "fields": {
            "name": "Sample Name",
            "description": "Sample Description"
        }
    }
]
```

Then, you can load this fixture in your tests using the `pytest.mark.django_db` decorator:

```python
# test_views.py

import pytest

@pytest.mark.django_db
@pytest.mark.usefixtures('sample_data')
def test_my_view():
    # Test logic here
```

**Run Tests Automatically**

You can automate the execution of your tests using continuous integration (CI) tools like Travis CI, Jenkins, or GitHub Actions. These tools can automatically run your tests whenever code changes are pushed to your repository.

By following these steps, you can set up a pre-configured testing environment in Django and use the pytest testing framework for robust test automation, making it easier to write and execute unit and integration tests for your Django applications.
