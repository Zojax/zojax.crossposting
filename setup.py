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
""" Setup for zojax.helpdesk package

$Id$
"""
import sys, os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version='0.1.0dev'


setup(name = 'zojax.article',
      version = version,
      author = 'Nikolay Kim',
      author_email = 'fafhrd91@gmail.com',
      description = "Helpdesk for z3ext.",
      long_description = (
          'Detailed Documentation\n' +
          '======================\n'
          + '\n\n' +
          read('CHANGES.txt')
          ),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Commercial License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
      url='http://zojax.com/',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['zojax',],
      install_requires = ['setuptools', 'rwproperty',
                          'z3ext.company',
                          'z3ext.content.actions',
                          'z3ext.content.space',
                          'z3ext.content.tagging',
                          'z3ext.content.discussion',
                          'z3ext.content.permissions',
                          'z3ext.content.notifications',
                          'z3ext.content.schema',
                          'z3ext.content.revision',
                          'z3ext.content.workflow',
                          'z3ext.principal.profile',
                          'z3ext.layout',
                          'z3ext.layoutform',
                          'z3ext.batching',
                          'z3ext.product',
                          'z3ext.company',
                          'z3ext.formatter',
                          'z3ext.statusmessage',
                          'z3ext.widget.checkbox',
                          'z3ext.mailin',
                          'zojax.report',
                          ],
      extras_require = dict(test=['zope.app.testing',
                                  'zope.app.zcmlfiles',
                                  'zope.testing',
                                  'zope.testbrowser',
                                  'zope.securitypolicy',
                                  'z3ext.autoinclude',
                                  'z3ext.security',
                                  'z3ext.personal.space',
                                  ]),
      include_package_data = True,
      zip_safe = False
      )
