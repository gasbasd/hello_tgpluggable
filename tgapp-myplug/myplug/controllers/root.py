# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import TGController, config
from tg import expose, flash, require, url, lurl, request, redirect, validate
import tg
from tg.i18n import ugettext as _
from myplug import model
from myplug.model import DBSession

class RootController(TGController):
    @expose('myplug.templates.index')
    def index(self):
        sample = DBSession.query(model.Sample).first()
        flash(_("Hello World!"))
        img1_url = tg.url('/_pluggable/myplug/images/too-easy.jpg')
        return dict(sample=sample, img1_url=img1_url)


    @expose('myplug.templates.index')
    def index_with_params(self):
        sample = DBSession.query(model.Sample).first()
        flash(_("Hello World!"))
        img1_url = config['_pluggable_myplug_config'].get('img1_url')
        return dict(sample=sample, img1_url=img1_url)

    @expose('myplug.templates.replace_template')
    def replace_template(self):
        return {}

    @expose('myplug.templates.patch_template')
    def patch_template(self):
        return {}

    @expose('myplug.templates.hooks')
    def hooks(self, **kw):
        user = request.identity['user']
        return {'user_name':user.display_name}