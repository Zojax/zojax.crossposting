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
from BTrees.Length import Length

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

from revision import RevisionItem
from interfaces import \
    IArticle, IArticleDraft, IArticleDrafts, IArticleManagement


class Article(PersistentItem, Revisions, RevisionItem):
    interface.implements(
        IArticle, IArticleManagement, IItemPublishing, IRevisions)

    __contentschema__ = IArticle
    __contentfields__ = {'text': RichTextProperty(IArticle['text']),
                         'abstract': RichTextProperty(IArticle['abstract'])}

    #text = RichTextProperty(IArticle['text'])
    #abstract = RichTextProperty(IArticle['abstract'])

    _revisions_length = Length(0)


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
