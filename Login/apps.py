from django.apps import AppConfig


class LoginConfig(AppConfig):
    name = 'Login'
    # Confiracion de nombre de la app en el manel de administracion
    # tenemos que darlo de alta en el setting.py para que Django tome esta configuracion
    # y la use en el panel de adminitracion >> 'Login.apps.LoginConfig'
    verbose_name = 'App Login'
