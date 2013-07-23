# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope.schema import TextLine


class IGSSiteName(Interface):
    name = TextLine(title=u'Site name',
      description=u'The name of your site. It will be used in the '
        u'body of pages, email messages, and at the top of every page.',
      required=True)
