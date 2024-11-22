#!/usr/bin/env python
from setuptools import setup

from clever_selects import VERSION

setup(
    name='django-clever-selects',
    version=VERSION,
    description='Chained select box widget for Django framework using AJAX requests.',
    long_description=open('README.rst').read(),
    author='Pragmatic Mates',
    author_email='info@pragmaticmates.com',
    maintainer='Pragmatic Mates',
    maintainer_email='info@pragmaticmates.com',
    url='https://github.com/PragmaticMates/django-clever-selects',
    packages=[
        'clever_selects',
        'clever_selects.templatetags'
    ],
    include_package_data=True,
    install_requires=('django>=3',),
    classifiers=[
        'Programming Language :: Python',
	      'Operating System :: OS Independent',
        'Environment :: Web Environment',        
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 5 - Production/Stable'
    ],
    license='BSD License',
    keywords="django clever chained selects ajax",
)
