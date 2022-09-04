import time

from plyer import notification

title = 'Hi, Hello and Hi !'

message = 'If u reading this ~I LOVE U TO THE MOON AND BACK !!'

notification.notify(title = title,
                    message = message,
                    app_icon = None,
                    timeout = 10,
                    toast = False)
