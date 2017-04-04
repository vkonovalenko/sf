from appname.modules.middleware.Middleware import Middleware


class Auth2(Middleware):

    def handle(self):
        print('handled middleware Auth2')
