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
from zope.schema.fieldproperty import FieldProperty
from zope.size import byteDisplay
from zope.size.interfaces import ISized
from zope.app.container.contained import NameChooser

from z3ext.content.type.item import PersistentItem
from z3ext.content.type.contenttype import ContentType
from z3ext.content.type.interfaces import IItemPublishing
from z3ext.richtext.field import RichTextProperty
from z3ext.filefield.field import FileFieldProperty
from z3ext.filefield.interfaces import IFile as IFileData

from revision import RevisionItem
from interfaces import IFile, IArticleDraft, IArticleDrafts, IArticleManagement


class File(PersistentItem, RevisionItem):
    interface.implements(IFile, IArticleManagement, IItemPublishing)

    data = FileFieldProperty(IFile['data'])
    abstract = RichTextProperty(IFile['abstract'])
    disposition = FieldProperty(IFile['disposition'])


class Sized(object):
    component.adapts(IFile)
    interface.implements(ISized)

    def __init__(self, context):
        self.context = context

    def sizeForSorting(self):
        return "byte", self.context.data.size

    def sizeForDisplay(self):
        return byteDisplay(self.context.data.size)


class FileType(ContentType):

    def add(self, content, name=''):
        if not name and content is not None:
            try:
                name = content.data.filename.split('\\')[-1].split('/')[-1]
            except AttributeError:
                pass
        return super(FileType, self).add(content, name)
