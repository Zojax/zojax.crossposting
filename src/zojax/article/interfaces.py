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
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zope.i18nmessageid import MessageFactory
from zojax.richtext.field import RichText
from zojax.filefield.field import FileField
from zojax.widget.radio.field import RadioChoice
from zojax.content.type.interfaces import IItem
from zojax.content.space.interfaces import IWorkspace, IWorkspaceFactory

_ = MessageFactory('zojax.article')


class IRevisionItem(interface.Interface):
    """ revision item """

    articleId = interface.Attribute('Article Id')
    articleRevId = interface.Attribute('Revision Id')
    articleSource = interface.Attribute('Source')
    articleDestination = interface.Attribute('Destination')
    articleActiveStatus = interface.Attribute('Active Revision')


class IArticle(IRevisionItem):
    """ article  """

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


dispositionVocabulary = SimpleVocabulary((
        SimpleTerm('attachment', 'attachment', _('Download')),
        SimpleTerm('inline', 'inline', _('View inline'))))


class IFile(IRevisionItem):

    title = schema.TextLine(
        title = _(u'Title'),
        description = _(u'File title.'),
        required = False)

    abstract = RichText(
        title = _(u'Abstract'),
        description = _(u'Article abstract.'),
        required = False)

    data = FileField(
        title=_(u'Data'),
        description=_(u'The actual content of the file.'),
        required = False)

    disposition = RadioChoice(
        title = _(u'How do you want to view this file.'),
        vocabulary = dispositionVocabulary,
        default = 'inline',
        required = True)


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
