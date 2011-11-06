from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='envparser',
      version=version,
      description="Simple environment configuration parser",
      long_description="""\
      See https://github.com/diogobaeder/envparser for documentation
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python environment parser configuration settings',
      author='Diogo Baeder',
      author_email='desenvolvedor@diogobaeder.com.br',
      url='https://github.com/diogobaeder/envparser',
      license='BSD 2-Clause',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
