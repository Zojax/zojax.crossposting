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
from zope.proxy import removeAllProxies
from zope.component import getUtility, queryMultiAdapter
from zope.dublincore.interfaces import IDCTimes
from zope.traversing.browser import absoluteURL
from zope.app.intid.interfaces import IIntIds
from zope.app.security.interfaces import IAuthentication, PrincipalLookupError

from z3ext.table.table import Table
from z3ext.table.column import Column, AttributeColumn
from z3ext.catalog.interfaces import ICatalog
from z3ext.formatter.utils import getFormatter
from z3ext.content.table.author import AuthorNameColumn
from zojax.article.interfaces import IArticle

from interfaces import _, IRevisionsTable


class RevisionsTable(Table):
    interface.implements(IRevisionsTable)
    component.adapts(IArticle, interface.Interface, interface.Interface)

    title = _('Revisions')

    pageSize = 15
    enabledColumns = ('id', 'principal', 'date', 'active')
    msgEmptyTable = _('No revisions.')
    cssClass = 'z-table z-content-revisions'

    def initDataset(self):
        self.dataset = getUtility(ICatalog).searchResults(
            noPublishing=True, showHidden=True,
            sort_on='articleRevId', sort_order='reverse',
            type = {'any_of': ('zojax.article',)},
            articleId = {'any_of': (self.context.articleId,)})


class IdColumn(Column):
    component.adapts(interface.Interface, interface.Interface, IRevisionsTable)

    name = 'id'
    title = _('Rev Id')
    cssClass = 'ctb-revision-revid'
    attrName = '__name__'

    def query(self, default=None):
        return '%0.3d'%int(self.content.__name__)

    def render(self):
        return u'<a href="%s/">%0.3d</a>'%(
            absoluteURL(self.content, self.request), self.content.articleRevId)


class PrincipalColumn(AuthorNameColumn):
    component.adapts(interface.Interface, interface.Interface, IRevisionsTable)

    title = _('User')
    cssClass = 'ctb-revisioin-principal'

    def getPrincipal(self, content):
        #return self.content.getPrincipal()
        return None


class DateColumn(Column):
    component.adapts(interface.Interface, interface.Interface, IRevisionsTable)

    name = 'date'
    title = _('Date')
    cssClass = 'ctb-revisioin-date'

    def query(self):
        return IDCTimes(self.context).modified

    def update(self):
        super(DateColumn, self).update()

        self.table.environ['fancyDatetime'] = getFormatter(
            self.request, 'fancyDatetime', 'medium')

    def render(self):
        value = self.query()
        if value:
            return self.globalenviron['fancyDatetime'].format(value)

        return u'---'


class ActiveColumn(Column):
    component.adapts(interface.Interface, interface.Interface, IRevisionsTable)

    name = 'active'
    title = _('Status')
    cssClass = 'ctb-revision-status'

    def query(self, default=None):
        if self.content.articleActiveStatus == 1:
            return u'Active'
        elif self.content.articleActiveStatus == 3:
            return u'Draft'
        return u'----'
