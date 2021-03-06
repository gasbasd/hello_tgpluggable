# -*- coding: utf-8 -*-
"""Setup the myplug application"""
from __future__ import print_function

from myplug import model
from tgext.pluggable import app_model

def bootstrap(command, conf, vars):
    print('Bootstrapping myplug...')

    s1 = model.Sample()
    s1.name = 'Test Sample'
    s1.user = model.DBSession.query(app_model.User).first()

    model.DBSession.add(s1)
    model.DBSession.flush()