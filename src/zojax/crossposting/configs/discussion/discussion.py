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
""" google ads portlet interfaces

$Id$
"""
from zope import interface
from z3c.pt.pagetemplate import ViewPageTemplateFile

from zojax.layout.pagelet import BrowserPagelet
from zojax.layoutform.subform import PageletEditSubForm
from zojax.layoutform import Fields


class AddComment(PageletEditSubForm):
    weight=9999


class AddCommentForm(BrowserPagelet):
    
    template = ViewPageTemplateFile('discussion.addcomment.pt')
