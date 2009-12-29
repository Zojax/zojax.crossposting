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
from zope.lifecycleevent import ObjectModifiedEvent
from zope.app.container.interfaces import INameChooser
from zope.app.component.hooks import getSite
from zope.app.intid.interfaces import IIntIds
from z3c.breadcrumb.interfaces import IBreadcrumb

from zojax.catalog.utils import listAllowedRoles
from zojax.catalog.interfaces import ICatalog
from zojax.content.type.interfaces import IContentType
from zojax.statusmessage.interfaces import IStatusMessage

from zojax.article.interfaces import _, IArticles, IArticleDraft


class PublishForm(object):

    def update(self):
        site = getSite()
        ids = getUtility(IIntIds)

        context = self.context
        request = self.request

        if u'form.button.publish' in request:
            try:
                id = int(request.get('destination', 0))
            except:
                id = 0
            dest = ids.queryObject(id)
            if dest is None or not checkPermission('zojax.AddArticle', dest):
                IStatusMessage(request).add(
                    _('Please select destination for this article.'))
            else:
                interface.noLongerProvides(
                    removeAllProxies(context), IArticleDraft)

                # set status
                articles = getUtility(ICatalog).searchResults(
                    noPublishing=True, noSecurityChecks=True, showHidden=True,
                    type = {'any_of': (IContentType(context).name,)},
                    articleId = {'any_of': (context.articleId,)})

                for article in articles:
                    if article.articleActiveStatus == 1:
                        removeAllProxies(article).articleActiveStatus = 2
                        event.notify(ObjectModifiedEvent(article))

                removeAllProxies(context).articleActiveStatus = 1

                # move to destination
                container = context.__parent__

                orig_name = context.__name__
                new_name = orig_name

                chooser = INameChooser(dest)
                new_name = chooser.chooseName(new_name, context)

                dest[new_name] = removeAllProxies(context)
                del container[orig_name]
                context = dest[new_name]

                IStatusMessage(request).add(_('Article has been published.'))
                self.redirect('%s/'%absoluteURL(context, request))
                return

        users = [id for id in listAllowedRoles(request.principal, site)]

        results = getUtility(ICatalog).searchResults(
            articleDestination={'any_of': users},
            type={'any_of': ('zojax.articles',)})

        articles = []

        for item in results:
            breadcrum = getMultiAdapter((item.__parent__, request), IBreadcrumb)

            id = ids.getId(item)
            info = {'title': item.title,
                    'id': id,
                    'selected': id == context.articleDestination,
                    'url': u'%s/'%absoluteURL(item, request),
                    'space': breadcrum.name,
                    'spaceUrl': breadcrum.url}

            articles.append((getPath(item), info))

        articles.sort()
        self.articles = [info for path, info in articles]
