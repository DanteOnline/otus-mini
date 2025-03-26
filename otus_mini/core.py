from jinja2 import Environment, FileSystemLoader, select_autoescape


class Application:

    def __init__(self):
        self.urls = {}

    def add_url(self, url, callback):
        self.urls[url] = callback

    def __call__(self, environ, start_response):
        # print('-------ENVIRON----------')
        # print(environ)
        # print('---------END ENVIROV-------')

        path_info = environ['PATH_INFO']
        status = "200 OK"
        headers = [("Content-Type", "text/html")]
        start_response(status, headers)

        callback = self.urls.get(path_info)


        if callback:
            result = callback()
        else:
            result = 'NOT FOUND'

        bytes_result = result.encode(encoding='utf-8')
        return [bytes_result]


application = Application()


# @application.add_url('/')
def index_view():
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape()
    )
    template = env.get_template("index.html")

    menu_list = [
        'Index1',
        'Contact',
    ]

    result = template.render(menu_list=menu_list)
    return result


# @application.add_url('/contacts')
def contact_view():
    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape()
    )

    template = env.get_template("contact.html")

    menu_list = [
        'Index',
        'Contact',
    ]

    result = template.render(menu_list=menu_list, contact_data='otus-mini')
    return result

application.add_url('/', index_view)
application.add_url('/contacts/', contact_view)
