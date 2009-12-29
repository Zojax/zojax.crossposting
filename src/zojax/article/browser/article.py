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
from zope.component import getUtility
from zope.traversing.browser import absoluteURL
from zope.dublincore.interfaces import IDCExtended
from zope.app.security.interfaces import IAuthentication

from zojax.ownership.interfaces import IOwnership
from zojax.principal.profile.interfaces import IPersonalProfile


class ArticleView(object):

    author = None

    def update(self):
        context = self.context
        request = self.request

        auth = getUtility(IAuthentication)

        ownership = IOwnership(context)
        owner = ownership.owner
        ownerId = ownership.ownerId

        if owner is not None:
            profile = IPersonalProfile(owner)
            self.author = {
                'id': ownerId,
                'title': profile.title,
                'space': profile.space is not None and u'%s/'%absoluteURL(
                    profile.space, request)
                }

        creators = []
        for pid in IDCExtended(context).creators:
            if pid != ownerId:
                try:
                    principal = auth.getPrincipal(pid)
                except:
                    continue

                profile = IPersonalProfile(principal)

                creators.append(
                    (profile.title,
                     {'id': pid,
                      'title': profile.title,
                      'space': profile.space is not None and u'%s/'%absoluteURL(
                                profile.space, request)}))

        creators.sort()
        self.creators = [info for t, info in creators]


class ArticleByLine(object):

    def isAvailable(self):
        return False
