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
from zope import interface, event
from zope.proxy import removeAllProxies
from zope.component import getUtility, getMultiAdapter
from zope.traversing.api import getPath
from zope.traversing.browser import absoluteURL
from zope.security import checkPermission
from zope.security.proxy import removeSecurityProxy
from zope.lifecycleevent import ObjectCopiedEvent
from zope.app.container.interfaces import INameChooser
from zope.app.component.hooks import getSite
from zope.app.intid.interfaces import IIntIds
from zc.copy import copy
from z3c.breadcrumb.interfaces import IBreadcrumb

from z3ext.catalog.utils import listAllowedRoles
from z3ext.catalog.interfaces import ICatalog
from z3ext.content.type.interfaces import IContentType
from z3ext.statusmessage.interfaces import IStatusMessage

from zojax.article.interfaces import _, IArticles, IArticleDraft


class NewRevisionForm(object):

    def update(self):
        site = getSite()
        ids = getUtility(IIntIds)

        context = self.context
        request = self.request

        if u'form.button.newrevision' in request:
            try:
                id = int(request.get('destination', 0))
            except:
                id = 0
            dest = ids.queryObject(id)
            if dest is None or not checkPermission('zojax.AddArticle', dest):
                IStatusMessage(request).add(
                    _('Please select destination for new revision.'))
            else:
                container = context.__parent__

                new_name = orig_name = context.__name__

                chooser = INameChooser(dest)
                new_name = chooser.chooseName(new_name, context)

                new = copy(removeAllProxies(context))
                new.articleRevId = None
                new.articleDestination = getUtility(IIntIds).getId(
                    removeAllProxies(container))

                # set revId
                revId = -1
                articles = getUtility(ICatalog).searchResults(
                    noPublishing=True, noSecurityChecks=True, showHidden=True,
                    type = {'any_of': (IContentType(context).name,)},
                    articleId = {'any_of': (context.articleId,)})

                for article in articles:
                    if article.articleRevId > revId:
                        revId = article.articleRevId

                new.articleRevId = revId + 1
                new.articleActiveStatus = 3

                event.notify(ObjectCopiedEvent(new, context))

                dest[new_name] = new
                context = dest[new_name]

                IStatusMessage(request).add(_('New revision has been created.'))
                self.redirect('%s/'%absoluteURL(context, request))
                return

        users = [id for id in listAllowedRoles(request.principal, site)]

        results = getUtility(ICatalog).searchResults(
            articleDestination={'any_of': users},
            type={'any_of': ('zojax.articledrafts',)})

        articles = []

        for item in results:
            breadcrum = getMultiAdapter((item.__parent__, request), IBreadcrumb)

            id = ids.getId(item)
            info = {'title': item.title,
                    'id': id,
                    'selected': id == context.articleSource,
                    'url': u'%s/'%absoluteURL(item, request),
                    'space': breadcrum.name,
                    'spaceUrl': breadcrum.url}

            articles.append((getPath(item), info))

        articles.sort()
        self.articles = [info for path, info in articles]
