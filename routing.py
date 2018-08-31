from channels.routing import route
from apps.portal.consumers import ws_connect, ws_disconnect, ws_message, msg_consumer

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
    route("websocket.receive", ws_message),
    route("ws-messages", msg_consumer),
]
