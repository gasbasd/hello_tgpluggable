from tg import expose

@expose('myplug.templates.little_partial')
def something(name):
    return dict(name=name)