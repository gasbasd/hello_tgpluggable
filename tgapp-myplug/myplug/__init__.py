# -*- coding: utf-8 -*-
"""The tgapp-myplug package"""

def plugme(app_config, options):
    app_config['_pluggable_myplug_config'] = options
    return dict(appid='myplug', global_helpers=False)