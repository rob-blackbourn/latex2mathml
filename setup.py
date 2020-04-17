
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='latex2mathml',
    version='2.10.1-alpha.0',
    description='Pure Python library for LaTeX to MathML conversion',
    python_requires='<4,>=3.5',
    project_urls={"repository": "https://github.com/roniemartinez/latex2mathml"},
    author='Ronie Martinez',
    author_email='ronmarti18@gmail.com',
    license='MIT',
    keywords='latex mathml',
    classifiers=['Development Status :: 5 - Production/Stable', 'License :: OSI Approved :: MIT License', 'Topic :: Scientific/Engineering :: Mathematics', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Processing :: Markup :: HTML', 'Topic :: Text Processing :: Markup :: LaTeX', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: Implementation :: CPython'],
    entry_points={"console_scripts": ["latex2mathml = latex2mathml.converter:main", "l2m = latex2mathml.converter:main"]},
    packages=['latex2mathml'],
    package_dir={"": "."},
    package_data={"latex2mathml": ["*.txt"]},
    install_requires=[],
    extras_require={"dev": ["bandit==1.*,>=1.6.2", "codecov==2.*,>=2.0.16", "flake8==3.*,>=3.7.9", "isort==4.*,>=4.3.21", "multidict==4.*,>=4.7.5", "pytest==5.*,>=5.3.5", "pytest-cov==2.*,>=2.8.1", "safety==1.*,>=1.8.7", "xmljson==0.*,>=0.2.0"]},
)
