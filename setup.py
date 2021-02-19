from distutils.core import setup

import setuptools

import registry

requirements = []

setup(name='rubix-registry',
      version=registry.__version__,
      author=registry.__author__,
      install_requires=requirements,
      description=registry.__doc__.strip(),
      python_requires='>=3.6',
      packages=setuptools.find_packages(),
      )
