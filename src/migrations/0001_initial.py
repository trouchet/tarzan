"""
Migration File: <generated_migration_file_name.py>

This migration file was generated by Django on <generated_timestamp> for creating
the 'Post' model and inserting initial data.

Migration Details:
- Creation of the 'Post' model with fields: 'id', 'title', 'content', and 'pub_date'.
- Insertion of sample data into the 'Post' model.

"""
# pylint: disable=invalid-name

from json import load

from django.db.migrations import Migration, CreateModel
from django.db.models import BigAutoField, CharField, TextField, DateTimeField
from django.db.migrations import RunPython

# Post model
post_fields = [
    (
        'id',
        BigAutoField(
            auto_created=True,
            primary_key=True,
            serialize=False,
            verbose_name='ID',
        ),
    ),
    ('title', CharField(max_length=200)),
    ('content', TextField()),
    ('pub_date', DateTimeField(verbose_name='date published')),
]
post_model_args = {
    'name': 'Post',
    'fields': post_fields,
}
post_operation = CreateModel(
    name=post_model_args['name'],
    fields=post_model_args['fields'],
)


# pylint: disable=unused-argument
def insert_posts(apps, schema_editor):
    """
    Insert Initial Data

    This function inserts sample data into the 'Post' model.

    Args:
        apps: A registry of applications.
        schema_editor: The schema editor used for the migration.

    """
    post_model = apps.get_model('src', 'Post')

    # Load sample data from a JSON file
    with open('./sample_posts.json', encoding='utf-8') as json_file:
        sample_data = load(json_file)

    # Insert the data into the 'Post' model
    for data in sample_data:
        post_model.objects.create(
            title=data['title'], content=data['content'], pub_date=data['pub_date']
        )


# pylint: disable=unused-argument
def reverse_insert_posts(apps, schema_editor):
    """
    Reverse Data Insertion

    This function can be used to reverse the data insertion if needed.

    Args:
        apps: A registry of applications.
        schema_editor: The schema editor used for the migration.

    """
    # If you need to reverse the data insertion, you can add DELETE or other
    # SQL statements here
    # pylint: disable=unnecessary-pass
    pass


# Available migrations
class Migrations(Migration):
    """
    Migration Class

    Django migration class for the 'src' app. It includes operations to create the 'Post' model and
    insert initial data.

    Attributes:
        initial (bool): Indicates if this is the initial migration for the app.
        dependencies (list): List of dependencies for this migration.
        operations (list): List of migration operations.

    """

    initial = True
    dependencies = []

    operations = [
        post_operation,
        RunPython(insert_posts, reverse_code=reverse_insert_posts),
    ]
