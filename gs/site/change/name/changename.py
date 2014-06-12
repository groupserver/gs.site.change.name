# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2012, 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import absolute_import, unicode_literals
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.base import SiteForm
from .interfaces import IGSSiteName


class ChangeName(SiteForm):
    label = 'Change the site name'
    pageTemplateFileName = 'browser/templates/changename.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(IGSSiteName, render_context=False)

    def __init__(self, context, request):
        super(ChangeName, self).__init__(context, request)

    def setUpWidgets(self, ignore_request=False):
        data = {'name': self.siteInfo.name, }
        self.widgets = form.setUpWidgets(
            self.form_fields, self.prefix, self.context,
            self.request, form=self, data=data,
            ignore_request=ignore_request)

    @form.action(label='Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        oldName = self.siteInfo.name
        self.siteInfo.siteObj.manage_changeProperties(title=data['name'])
        self.status = 'The of this site has been '\
            'changed to <q>%s</a> from <q>%s</q>.' % \
            (data['name'], oldName)

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = '<p>There is an error:</p>'
        else:
            self.status = '<p>There are errors:</p>'
