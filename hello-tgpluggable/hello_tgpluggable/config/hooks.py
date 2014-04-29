import tg


class MyPlugHooks(object):

    @classmethod
    def register(cls, base_config):
        tg.hooks.register('myplug.my_hook', cls.my_hook)

    @classmethod
    def my_hook(cls, user):
        user.display_name = 'Simone'
