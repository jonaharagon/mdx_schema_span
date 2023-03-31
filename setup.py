#! /usr/bin/env python

from setuptools import setup
setup(
    name='mdx_schema_span',
    version='1.0.0',
    author='Jonah Aragon',
    author_email='jonah@triplebit.net',
    description='A Markdown extension for specifying schema.org sameAs to strings.',
    url='https://github.com/jonaharagon/mdx_schema_span',
    py_modules=['mdx_schema_span'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
