from jinja2 import Environment, FileSystemLoader, select_autoescape


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
