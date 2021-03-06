from pyramid.view import view_config

#configuration decoration


@view_config(route_name='emptypath', renderer='templates/index.jinja2') # binds handler to the view
def empty_path(request):
    return {'link': '<a href="about/aboutme.html">to about me page</a>'}

@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    return {'link': '<a href="about/aboutme.html">to about me page</a>'}

@view_config(route_name='about', renderer='templates/about/aboutme.jinja2')
def aboutme(request):
    return {'link': """<a href="../index.html">to about me page</a>"""}
