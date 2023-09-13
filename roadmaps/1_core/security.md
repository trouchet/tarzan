Implementing essential security measures in a Django application is crucial to protect it from common vulnerabilities. Here's how you can perform these actions:

Implement Essential Security Measures:

a. CSRF Protection: Django provides built-in CSRF protection. Ensure that the {% csrf_token %} template tag is included in all your forms. Django middleware automatically handles CSRF protection.
b. XSS Prevention: Django template engine automatically escapes variables to prevent Cross-Site Scripting (XSS) attacks. However, make sure that you don't mark content as safe using |safe filter unless you're absolutely certain it's safe.

Use Secure Password Handling Techniques:

a. Bcrypt or Argon2: Django uses the PBKDF2 algorithm for password hashing by default, which is considered secure. However, you can enhance security by using third-party packages like bcrypt or argon2-cffi for password hashing.
b. Update Django Settings: To use a different password hashing algorithm, update the PASSWORD_HASHERS setting in your Django project's settings file. For example, to use bcrypt, you can set it as follows:

```python
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    # ...
]
```

Add Rate Limiting and IP Blocking:

a. Rate Limiting: You can implement rate limiting to thwart brute-force attacks by using Django's built-in ratelimit decorator or middleware. Here's an example of using the ratelimit decorator:

```python
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page

@csrf_exempt  # Disable CSRF protection for this view
@cache_page(60)  # Limit requests to one per minute
def login(request):
    # Your login logic here
```

b. IP Blocking: To block IPs after repeated failed login attempts, you can implement custom middleware or use third-party packages like django-axes. django-axes allows you to configure IP blocking thresholds and actions.

Install django-axes using pip:

```bash
pip install django-axes
```

Add it to your Django project's settings:

```python
MIDDLEWARE = [
    # ...
    'axes.middleware.AxesMiddleware',
    # ...
]

# Configure axes
AXES_FAILURE_LIMIT = 3  # Number of login failures before blocking
AXES_LOCKOUT_TEMPLATE = 'path_to_your_custom_lockout_template.html'
```

You can also set IP blocking duration, logging, and other options in the settings.

Remember to monitor your application's logs and security reports regularly to stay informed about potential security threats and vulnerabilities. Additionally, keep your Django and third-party packages up to date to benefit from the latest security patches and improvements.