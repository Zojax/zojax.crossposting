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
from zope import interface, schema
from zope.i18nmessageid import MessageFactory
from z3ext.richtext.field import RichText
from z3ext.content.type.interfaces import IItem
from z3ext.content.space.interfaces import IWorkspace, IWorkspaceFactory

_ = MessageFactory('zojax.article')


class IArticle(interface.Interface):
    """ article  """

    articleId = interface.Attribute('Article Id')
    articleRevId = interface.Attribute('Revision Id')
    articleSource = interface.Attribute('Source')
    articleDestination = interface.Attribute('Destination')
    articleActiveStatus = interface.Attribute('Active Revision')

    title = schema.TextLine(
        title = _('Title'),
        description = _('Article title.'),
        default = u'',
        missing_value = u'',
        required = True)

    abstract = RichText(
        title = _(u'Abstract'),
        description = _(u'Article abstract.'),
        required = False)

    text = RichText(
        title = _(u'Text'),
        description = _(u'Article text.'),
        required = True)

    def getSource():
        """ get source object """

    def getDestination():
        """ return destination object """


class IArticleDraft(interface.Interface):
    """ marker interface for article draft """


class IArticleManagement(interface.Interface):
    """ article management interface """

    def publish():
        """ publish article """

    def isPublishable():
        """ """

    def makeRevision():
        """ make revision, return new draft article """



class IArticles(IItem, IWorkspace):
    """ Articles workspace """


class IArticlesFactory(IWorkspaceFactory):
    """ Articles workspace factory """


class IArticleDrafts(IItem, IWorkspace):
    """ drafts container """


class IArticleDraftsFactory(IWorkspaceFactory):
    """ article drafts workspace factory """
