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
from zope.size import byteDisplay
from zope.size.interfaces import ISized
from zope.component import getUtility
from zope.security import checkPermission
from zope.app.intid.interfaces import IIntIds, IIntIdAddedEvent
from z3ext.catalog.interfaces import ICatalog
from z3ext.content.type.item import PersistentItem
from z3ext.content.type.interfaces import IItemPublishing
from z3ext.content.type.searchable import ContentSearchableText
from z3ext.richtext.field import RichTextProperty
from z3ext.content.revision.revisions import Revisions, IRevisions

from interfaces import \
    IArticle, IArticleDraft, IArticleDrafts, IArticleManagement

from BTrees.Length import Length

class Article(PersistentItem, Revisions):
    interface.implements(
        IArticle, IArticleManagement, IItemPublishing, IRevisions)

    __contentschema__ = IArticle
    __contentfields__ = {'text': RichTextProperty(IArticle['text']),
                         'abstract': RichTextProperty(IArticle['abstract'])}

    #text = RichTextProperty(IArticle['text'])
    #abstract = RichTextProperty(IArticle['abstract'])

    articleId = None
    articleRevId = None
    articleSource = None
    articleDestination = None
    articleActiveStatus = 3 # 1 - active, 2 - not active, 3 - draft

    _revisions_length = Length(0)


@component.adapter(IArticle, IIntIdAddedEvent)
def articleAddedHandler(article, event):
    ids = getUtility(IIntIds)

    if article.articleId is None:
        article.articleId = ids.getId(article)

    if article.articleSource is None:
        article.articleSource = ids.getId(article.__parent__)

    if IArticleDrafts.providedBy(article.__parent__):
        interface.alsoProvides(article, IArticleDraft)

    if article.articleRevId is None:
        revId = -1
        articles = getUtility(ICatalog).searchResults(
            noPublishing=True, noSecurityChecks=True,
            type = {'any_of': ('zojax.article',)},
            articleId = {'any_of': (article.articleId,)})

        for article in articles:
            if article.articleRevId > revId:
                revId = article.articleRevId

        article.articleRevId = revId + 1


class Sized(object):
    component.adapts(IArticle)
    interface.implements(ISized)

    def __init__(self, context):
        self.context = context

        self.size = len(context.title) + \
            len(context.abstract) + \
            len(context.text)

    def sizeForSorting(self):
        return "byte", self.size

    def sizeForDisplay(self):
        return byteDisplay(self.size)


class ArticleSearchableText(ContentSearchableText):
    component.adapts(IArticle)

    def getSearchableText(self):
        text = super(ArticleSearchableText, self).getSearchableText()
        try:
            return text + u' ' + self.content.text.text
        except AttributeError:
            return text
