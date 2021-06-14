from distutils.core import setup
from os.path import join, dirname

import setuptools

import registry

with open(join(dirname(__file__), 'requirements.txt'), 'r') as f:
    install_requires = f.read().split("\n")

setup(name='rubix-registry',
      version=registry.__version__,
      author=registry.__author__,
      description=registry.__doc__.strip(),
      python_requires='>=3.6',
      packages=setuptools.find_packages(),
      install_requires=install_requires,
      )
