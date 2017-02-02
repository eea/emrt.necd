from setuptools import setup, find_packages
import os

version = open('version.txt').read().strip()

setup(
    name='emrt.necd',
    version=version,
    description="EMRT-NECD Customisation package",
    long_description=(
        open("README.rst").read() + "\n" +
        open(os.path.join("docs", "HISTORY.txt")).read()
    ),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Zope2",
    ],
    keywords='emrt necd customisation package',
    author='David Batranu',
    author_email='david.batranu@eaudeweb.ro',
    url='https://github.com/eea/emrt.necd',
    license='GPL-3.0',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['emrt'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'esdrt.theme',
        'esdrt.content',
    ],
    extras_require={
    },
    entry_points="""
      # -*- Entry points: -*-
      """,
)
