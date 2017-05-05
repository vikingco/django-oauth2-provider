#!/usr/bin/env python

from setuptools import setup, find_packages
import provider

# Running our own version as upstream seems to be abandoned.
setup(
    name='django-oauth2-provider-unleashed',
    version=provider.__version__,
    url='https://github.com/vikingco/django-oauth2-provider',
    license='MIT',
    description='Provide OAuth2 access to your app',
    long_description=open('README.rst').read(),
    author='Alen Mujezinovic',
    author_email='alen@caffeinehit.com',
    maintainer='Unleashed NV',
    maintainer_email='operations@unleashed.be',
    packages=find_packages(exclude=('tests*',)),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    install_requires=[
        'shortuuid>=0.3',
    ],
)
