##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
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
"""

$Id$
"""
from zope import interface, component
from zope.location import LocationProxy
from zope.traversing.browser import absoluteURL
from zope.publisher.interfaces import NotFound
from z3ext.content.actions.action import Action
from zojax.article.interfaces import IArticle

from interfaces import _, IRevisionsAction


class RevisionsAction(Action):
    component.adapts(IArticle, interface.Interface)
    interface.implements(IRevisionsAction)

    weight = 901
    title = _(u'Article Revisions')
    permission = 'zope.View' #.ViewContentRevisions'

    @property
    def url(self):
        return '%s/articlerevisions/'%absoluteURL(self.context, self.request)


class RevisionsView(object):

    title = _('Article revisions')

    def publishTraverse(self, request, name):
        try:
            return LocationProxy(
                self.context.getRevision(int(name)), self, name)
        except Exception, err:
            pass

        raise NotFound(self, request, name)
