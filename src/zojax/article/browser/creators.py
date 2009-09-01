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
from zope import schema, interface
from zope.dublincore.interfaces import IDCExtended

from z3ext.layoutform import Fields
from z3ext.wizard.step import WizardStepForm
from z3ext.wizard.interfaces import ISaveable
from z3ext.principal.field import UserField
from z3ext.ownership.interfaces import IOwnership


class ICreators(interface.Interface):

    creators = schema.Tuple(
        title = u'Select authors',
        value_type = UserField(),
        required = False)


class CreatorsEditForm(WizardStepForm):
    interface.implements(ISaveable)

    fields = Fields(ICreators)
    weight = 110
    
    title = u'Co-authors'
    label = u'Change co-authors list'

    def getContent(self):
        creators = IDCExtended(self.context).creators

        owner = IOwnership(self.context)
        if owner.ownerId in creators:
            creators = list(creators)
            creators.remove(owner.ownerId)

        return {'creators': tuple(creators)}

    def applyChanges(self, data):
        owner = IOwnership(self.context)
        if owner.ownerId not in data['creators']:
            data['creators'] = data['creators'] + (owner.ownerId,)

        dc = IDCExtended(self.context)
        if dc.creators != data['creators']:
            dc.creators = [unicode(s) for s in data['creators']]
            return True

        return False
