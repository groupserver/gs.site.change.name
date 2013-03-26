# -*- coding: utf-8 -*-
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.form import SiteForm
from interfaces import IGSSiteName


class ChangeName(SiteForm):
    label = u'Change the Site Name'
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

    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        oldName = self.siteInfo.name
        self.siteInfo.siteObj.manage_changeProperties(title=data['name'])
        self.status = u'The of this site has been '\
            'changed to <q>%s</a> from <q>%s</q>.' % \
            (data['name'], oldName)
        assert type(self.status) == unicode

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'
        assert type(self.status) == unicode
