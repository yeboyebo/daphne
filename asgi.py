"""
ASGI config for AQNEXT project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
from channels.asgi import get_channel_layer
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AQNEXT.settings")

channel_layer = get_channel_layer()
