from os import path
import sys

PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))

sys.path.insert(0, path.join(PROJECT_ROOT, "../../../motor/"))
sys.path.insert(1, path.join(PROJECT_ROOT, "apps/"))

from YBAQNEXT.settings import *
from YBAQNEXT.yeboapps import *
from .local import *

INSTALLED_APPS += ('channels', )

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgi_rabbitmq.RabbitmqChannelLayer',
        'ROUTING': 'AQNEXT.routing.channel_routing',
        'CONFIG': {
            'url': 'amqp://desarrollo:desarrollo@localhost:5672/desarrollo'
        },
    },
}
