#!/usr/bin/env python
from setuptools import setup, find_packages


setup(name='oao25',
      description='observing with adaptive optics school',
      version='0.1.1',
      long_description="Observing with Adaptive Optics summer school 2024",
      url='',
      license='MIT',
      keywords='adaptive optics',
      packages=find_packages(),
      install_requires=["numpy",
                        "astropy",
                        ],
      test_suite='test',
      package_data={
          'oao25': ['data/*'],
      },
      include_package_data=True,
      )