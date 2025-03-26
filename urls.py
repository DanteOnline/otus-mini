from otus_mini import Application
import views


application = Application()

application.add_url('/', views.index_view)
application.add_url('/contacts/', views.contact_view)


def simple_debug_middleware(old_application):

    def new_application(environ, start_response):
        print('TEST DEBUG MODE')
        return old_application(environ, start_response)

    return new_application


def debug_middleware(old_application):

    def new_application(environ, start_response):
        print('PATH_INFO', environ.get('PATH_INFO'))
        return old_application(environ, start_response)

    return new_application


application = debug_middleware(simple_debug_middleware(application))
