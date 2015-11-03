#! /usr/bin/env python
from distutils.core import setup
from setuptools import find_packages


setup(
    name='django_filebrowser_extension',
    version='0.0.2',
    author='Tomasz Roszko',
    author_email='tomaszroszko@tjsoftware.co',
    description='Extension for django-filebrowser',
    long_description=open('README.md').read(),
    url='https://github.com/tomaszroszko/django_filebrowser_extension',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
    ],
)
