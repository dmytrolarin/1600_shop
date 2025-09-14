import flask


def render_catalog():
    return flask.render_template(template_name_or_list="catalog.html")