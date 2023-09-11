from django.apps import apps
from src.apps import MyappConfig

def test_app_config_attributes():
    # Get the app config instance
    app_config = apps.get_app_config('src')

    # Check the attributes
    assert app_config.default_auto_field == 'django.db.models.BigAutoField'    
    assert app_config.name == 'src'
