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
from zope.security.proxy import removeSecurityProxy
from zc.catalog.catalogindex import ValueIndex, SetIndex
from z3ext.content.type.interfaces import IContentType
from z3ext.catalog.utils import Indexable, getAccessList

from interfaces import IArticle, IRevisionItem


def articleId():
    return ValueIndex('articleId', IRevisionItem)

def articleRevId():
    return ValueIndex('articleRevId', IRevisionItem)

def articleActiveStatus():
    return ValueIndex('articleActiveStatus', IRevisionItem)

def articleDestination():
    return SetIndex(
        'value', Indexable('zojax.article.indexes.ArticleDestination'))


class ArticleDestination(object):

    def __init__(self, context, default=None):
        self.value = default

        _context = removeSecurityProxy(context)

        ct = IContentType(_context, None)
        if ct is None or \
                ct.name not in ('zojax.articles', 'zojax.articledrafts'):
            return

        self.value = [user for user in
                      getAccessList(_context, 'zojax.AddArticle')]
