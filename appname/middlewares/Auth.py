from appname.modules.middleware.Middleware import Middleware


class Auth(Middleware):

    def handle(self):
        print('handled middleware Auth')
