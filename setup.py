#!/usr/bin/env python
from setuptools import setup

req = ['python-dateutil','pytz','nose','numpy','scipy','xarray','h5py','astropy','matplotlib','seaborn',
      'sciencedates',
        'pathvalidate']


setup(name='gridaurora',
      packages=['gridaurora'],
      author='Michael Hirsch, Ph.D.',
      description='Gridding for auroral and ionospheric modeling',
      url='https://github.com/scivision/gridaurora',
      version='0.5',
      data_files=[('gridaurora/data',['RecentIndices.txt'])],
	  install_requires=req,
      extras_require={'lowtran':'lowtran'}, #optional
      package_data={'gridaurora.precompute': ['*.h5']},
      classifiers=[
          'Intended Audience :: Science/Research',
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Topic :: Scientific/Engineering :: Atmospheric Science',
          'Programming Language :: Python :: 3',
          ],
	  )

