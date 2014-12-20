#!/usr/bin/env python

from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='saltshaker',
      version='0.0.1',
      description='Development environment provisioning with Salt made easy. Just Shaker it!',
      long_description=readme(),
      url='https://github.com/diegotoral/SaltShaker',
      author='Diego Toral',
      author_email='diegotoral@gmail.com',
      license='MIT',
      packages=['saltshaker'],
      keywords='saltshaker salt provisioning',
      scripts=['scripts/shaker'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
