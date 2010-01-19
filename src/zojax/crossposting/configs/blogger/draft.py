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
from zope.traversing.browser import absoluteURL

from zojax.content.forms.interfaces import IAddContentWizard
from zojax.layoutform.subform import PageletEditSubForm
from zojax.layoutform import Fields


class AddBlogPost(PageletEditSubForm):

    url = ''

    def update(self):
        super(AddBlogPost, self).update()
        if not self.isAvailable():
            return
        location = self.parentForm.wizard.draft.getLocation()
        if location is not None:
            self.url = absoluteURL(location, self.request)

    def isAvailable(self):
        return IAddContentWizard.providedBy(self.parentForm.wizard)
