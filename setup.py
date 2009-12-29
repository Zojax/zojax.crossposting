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
      description = "Helpdesk for zojax.",
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
                          'zojax.company',
                          'zojax.content.actions',
                          'zojax.content.space',
                          'zojax.content.tagging',
                          'zojax.content.discussion',
                          'zojax.content.permissions',
                          'zojax.content.notifications',
                          'zojax.content.schema',
                          'zojax.content.revision',
                          'zojax.content.workflow',
                          'zojax.principal.profile',
                          'zojax.layout',
                          'zojax.layoutform',
                          'zojax.batching',
                          'zojax.product',
                          'zojax.company',
                          'zojax.formatter',
                          'zojax.statusmessage',
                          'zojax.widget.checkbox',
                          'zojax.mailin',
                          'zojax.report',
                          ],
      extras_require = dict(test=['zope.app.testing',
                                  'zope.app.zcmlfiles',
                                  'zope.testing',
                                  'zope.testbrowser',
                                  'zope.securitypolicy',
                                  'zojax.autoinclude',
                                  'zojax.security',
                                  'zojax.personal.space',
                                  ]),
      include_package_data = True,
      zip_safe = False
      )
