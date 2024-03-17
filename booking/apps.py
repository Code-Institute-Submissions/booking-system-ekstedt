from django.apps import AppConfig


class BookingConfig(AppConfig):
    """
    AppConfig for the 'booking' Django app.

    This class provides configuration settings for the 'booking' app.
    It is used to define metadata and settings specific to the app.

    Attributes:
        default_auto_field (str):
        The default auto-increment field to be used for model primary keys.
        In this case, it is set to 'django.db.models.BigAutoField'.
        name (str): The name of the app, which is 'booking' in this case.

    Note:
        This class is used to customize app-level behavior and settings.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
