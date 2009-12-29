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
from zope.traversing.browser import absoluteURL
from zojax.content.actions.action import Action
from zojax.content.actions.categories import ActionCategory

from zojax.article.interfaces import _, IRevisionItem, IArticle, IArticleDraft

from interfaces import \
    IPublishArticleAction, INewRevisionAction, IContentRevisionsCategory


ContentRevisions = ActionCategory(
    _(u'Article revisions'), 25, IContentRevisionsCategory)


class PublishArticleAction(Action):
    interface.implements(IPublishArticleAction)
    component.adapts(IArticleDraft, interface.Interface)

    title = _('Publish')
    permission = 'zojax.ManageArticle'
    weight = 900

    @property
    def url(self):
        return u'%s/publish.html'%absoluteURL(self.context, self.request)


class NewArticleRevisionAction(Action):
    interface.implements(INewRevisionAction)
    component.adapts(IRevisionItem, interface.Interface)

    title = _('New Revision')
    permission = 'zojax.ManageArticle'
    weight = 900

    @property
    def url(self):
        return u'%s/newrevision.html'%absoluteURL(self.context, self.request)

    def isAvailable(self):
        if super(NewArticleRevisionAction, self).isAvailable() and \
                not IArticleDraft.providedBy(self.context):
            return True
        return False
