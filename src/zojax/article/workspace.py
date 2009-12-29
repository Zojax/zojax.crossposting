##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
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
from zope import interface, component, event
from zope.security.proxy import removeSecurityProxy
from zojax.content.type.container import ContentContainer
from zojax.content.space.interfaces import IContentSpace
from zojax.content.space.workspace import WorkspaceFactory

from interfaces import _, IArticles, IArticlesFactory


class Articles(ContentContainer):
    interface.implements(IArticles)

    @property
    def space(self):
        return self.__parent__


class ArticlesFactory(WorkspaceFactory):
    component.adapts(IContentSpace)
    interface.implements(IArticlesFactory)

    name = 'articles'
    title = _(u'Articles')
    description = _(u'Articles workspace.')
    weight = 90
    factory = Articles
