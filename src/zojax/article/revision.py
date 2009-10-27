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
from zope.component import getUtility
from zope.app.intid.interfaces import IIntIds, IIntIdAddedEvent
from z3ext.catalog.interfaces import ICatalog
from z3ext.content.type.interfaces import IContentType

from interfaces import IRevisionItem, IArticleDraft, IArticleDrafts


class RevisionItem(object):

    articleId = None
    articleRevId = None
    articleSource = None
    articleDestination = None
    articleActiveStatus = 3 # 1 - active, 2 - not active, 3 - draft


@component.adapter(IRevisionItem, IIntIdAddedEvent)
def revisionItemAddedHandler(article, event):
    ids = getUtility(IIntIds)

    if article.articleId is None:
        article.articleId = ids.getId(article)

    if article.articleSource is None:
        article.articleSource = ids.getId(article.__parent__)

    if IArticleDrafts.providedBy(article.__parent__):
        interface.alsoProvides(article, IArticleDraft)

    if article.articleRevId is None:
        revId = 0
        articles = getUtility(ICatalog).searchResults(
            noPublishing=True, noSecurityChecks=True,
            type = {'any_of': (IContentType(article).name,)},
            articleId = {'any_of': (article.articleId,)})

        for article in articles:
            if article.articleRevId > revId:
                revId = article.articleRevId

        article.articleRevId = revId + 1
