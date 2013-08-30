# -*- coding: utf-8 -*-
"""
This module contains the osha.translations package
"""
from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '2.0.16.dev0'

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    read('src', 'osha', 'translations', 'README.txt')
    )

setup(name='osha.translations',
      version=version,
      description="i18n translations for EU-OSHA",
      long_description=long_description,
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)",
        ],
      keywords='',
      author='European Agency for Safety and Health at Work, Syslab.com GmbH',
      author_email='info@syslab.com',
      url='http://www.syslab.com',
      license='GPL + EUPL',
      packages=['osha', 'osha/translations'],
      package_dir={'': 'src'},
      namespace_packages=['osha'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      extras_require={
          'podiff': ['polib'],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      [console_scripts]
      podiff = osha.translations:podiff
      """,
      )
