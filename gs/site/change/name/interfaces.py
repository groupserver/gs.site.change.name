# -*- coding: utf-8 -*-
############################################################################
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
############################################################################
from __future__ import unicode_literals
from zope.interface import Interface
from zope.schema import TextLine
from . import GSMessageFactory as _


class IGSSiteName(Interface):
    name = TextLine(
        title=_('site-name-entry-label', 'Site name'),
        description=_('site-name-entry-description',
                      'The name of your site. It will be used in the body '
                      'of pages, email messages, and at the top of every '
                      'page.'),
        required=True)
