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
from z3ext.content.space.workspace import WorkspaceFactory

from workspace import Articles
from interfaces import _, IArticleDraft, IArticleDrafts, IArticleDraftsFactory


class ArticleDrafts(Articles):
    interface.implements(IArticleDrafts)


class ArticleDraftsFactory(WorkspaceFactory):
    interface.implements(IArticleDraftsFactory)

    name = 'articledrafts'
    title = _(u'Article drafts')
    description = _(u'Article drafts workspace.')
    weight = 91
    factory = ArticleDrafts
